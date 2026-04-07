import pygame
import random
import math

MIN_SIZE = 10
MAX_SIZE = 40
MAX_SPEED = 5
JITTER_CHANCE = 0.05
JITTER_ANGLE = 30
FPS = 60

DETECTION_RANGE = 100
SIZE_THRESHOLD = 5
FLEE_FORCE = 2.0


class Square:
    """Represents a moving square on the canvas"""

    def __init__(self, x, y, size, color, velocity_x, velocity_y):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.jitter_counter = 0

    def detect_larger_squares(self, all_squares):
        """Detect all larger squares within detection range"""
        threats = []
        for other in all_squares:
            if other is self:
                continue
            if other.size <= self.size + SIZE_THRESHOLD:
                continue
            distance = math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
            if distance < DETECTION_RANGE:
                threats.append(other)
        return threats

    def calculate_flee_vector(self, threats):
        """Calculate flee vector away from all threats"""
        flee_x = 0.0
        flee_y = 0.0
        
        for threat in threats:
            dx = self.x - threat.x
            dy = self.y - threat.y
            distance = math.sqrt(dx**2 + dy**2)
            
            if distance == 0:
                distance = 1  
            
            norm_x = dx / distance
            norm_y = dy / distance
            
            force = (DETECTION_RANGE - distance) / DETECTION_RANGE
            force = max(0, force)  
            
            flee_x += norm_x * force * FLEE_FORCE
            flee_y += norm_y * force * FLEE_FORCE
        
        return (flee_x, flee_y)

    def update(self, all_squares):
        threats = self.detect_larger_squares(all_squares)
        
        flee = self.calculate_flee_vector(threats)
        
        self.velocity_x += flee[0]
        self.velocity_y += flee[1]
        
        speed = math.sqrt(self.velocity_x**2 + self.velocity_y**2)
        if speed > MAX_SPEED:
            scale = MAX_SPEED / speed
            self.velocity_x *= scale
            self.velocity_y *= scale
        
        self.x += self.velocity_x
        self.y += self.velocity_y
        
        self.apply_jitter()

    def apply_jitter(self):
        """Apply random rotation to velocity vector for jitter effect"""
        if random.random() < JITTER_CHANCE:
            speed = math.sqrt(self.velocity_x**2 + self.velocity_y**2)

            if speed == 0:
                return

            current_angle = math.atan2(self.velocity_y, self.velocity_x)

            jitter_rotation = random.uniform(-JITTER_ANGLE, JITTER_ANGLE)
            jitter_radians = math.radians(jitter_rotation)
            new_angle = current_angle + jitter_radians

            self.velocity_x = speed * math.cos(new_angle)
            self.velocity_y = speed * math.sin(new_angle)

    def draw(self, surface):
        pygame.draw.rect(
            surface, self.color, pygame.Rect(self.x, self.y, self.size, self.size)
        )

    def check_boundaries(self, width, height):
        if self.x < 0 or self.x + self.size > width:
            self.velocity_x *= -1

        if self.y < 0 or self.y + self.size > height:
            self.velocity_y *= -1


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Squares")

clock = pygame.time.Clock()


squares = []

for _ in range(10):
    size = random.randint(MIN_SIZE, MAX_SIZE)

    x = random.randint(0, SCREEN_WIDTH - size)
    y = random.randint(0, SCREEN_HEIGHT - size)

    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    speed = (MAX_SIZE - size) / (MAX_SIZE - MIN_SIZE) * MAX_SPEED

    angle = random.uniform(0, 2 * math.pi)
    velocity_x = speed * math.cos(angle)
    velocity_y = speed * math.sin(angle)

    if abs(velocity_x) > MAX_SPEED:
        velocity_x = MAX_SPEED if velocity_x > 0 else -MAX_SPEED
    if abs(velocity_y) > MAX_SPEED:
        velocity_y = MAX_SPEED if velocity_y > 0 else -MAX_SPEED

    square = Square(x, y, size, color, velocity_x, velocity_y)
    squares.append(square)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for square in squares:
        square.update(all_squares=squares)
        square.check_boundaries(SCREEN_WIDTH, SCREEN_HEIGHT)

    screen.fill((255, 255, 255))

    for square in squares:
        square.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
