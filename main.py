import pygame
import random
import math
from typing import List, Tuple, Optional

MAX_SPEED = 300
JITTER_CHANCE = 0.05
JITTER_ANGLE = 30
FPS = 60
DETECTION_RANGE = 100
SIZE_THRESHOLD = 5
FLEE_FORCE = 2.0
CHASE_FORCE = 2.0
MIN_SIZE = 4
MAX_SIZE = 25
MID_SIZE = 10
TRAILS_LENGTH = 30

class Square:
    def __init__(self, x: float, y: float, size: int, color: Tuple[int, int, int], 
                 vx: float, vy: float, birth_time: float):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.velocity_x = vx
        self.velocity_y = vy
        self.birth_time = birth_time
        self.lifespan = random.uniform(3.0, 9.0)
        self.trail: List[Tuple[float, float]] = []  

    def check_collision(self, other: 'Square') -> bool:
        """EX 4: Returns true if self and other collide using Pygame Rects[cite: 1]."""
        rect1 = pygame.Rect(self.x, self.y, self.size, self.size)
        rect2 = pygame.Rect(other.x, other.y, other.size, other.size)
        return rect1.colliderect(rect2)

    def check_boundaries(self, width: int, height: int) -> None:
        """EX 3: Screen Wrapping Feature[cite: 1]."""
        if self.x < 0: self.x = width
        elif self.x > width: self.x = 0
        if self.y < 0: self.y = height
        elif self.y > height: self.y = 0

    def update(self, all_squares: List['Square'], delta_time: float):
        avg_size = (MIN_SIZE + MAX_SIZE + MID_SIZE) / 3
        
        move_x, move_y = 0.0, 0.0

        self.velocity_x += move_x
        self.velocity_y += move_y

        self.trail.append((self.x + self.size/2, self.y + self.size/2))
        if len(self.trail) > TRAILS_LENGTH:
            self.trail.pop(0)

        self.x += self.velocity_x * delta_time
        self.y += self.velocity_y * delta_time
        self.apply_jitter()

    def apply_jitter(self):
        if random.random() < JITTER_CHANCE:
            angle = math.atan2(self.velocity_y, self.velocity_x)
            angle += math.radians(random.uniform(-JITTER_ANGLE, JITTER_ANGLE))
            speed = math.hypot(self.velocity_x, self.velocity_y)
            self.velocity_x = math.cos(angle) * speed
            self.velocity_y = math.sin(angle) * speed

    def draw(self, surface: pygame.Surface):
        if len(self.trail) > 1:
            for i in range(len(self.trail) - 1):
                p1, p2 = self.trail[i], self.trail[i+1]
                if math.dist(p1, p2) < 100: 
                    pygame.draw.line(surface, self.color, p1, p2, 2)
        
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))

    def is_dead(self, current_time: float) -> bool:
        return (current_time - self.birth_time) > self.lifespan

def create_random_square(birth_time: float, size: Optional[int] = None) -> Square:
    """EX 1 & 2: Support specific size creation[cite: 1]."""
    s = size if size is not None else random.randint(MIN_SIZE, MAX_SIZE)
    x = random.randint(0, 800 - s)
    y = random.randint(0, 600 - s)
    color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
    angle = random.uniform(0, 2 * math.pi)
    speed = random.uniform(50, MAX_SPEED)
    return Square(x, y, s, color, math.cos(angle)*speed, math.sin(angle)*speed, birth_time)

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
elapsed_time = 0.0

squares = []
for s, count in [(25, 5), (10, 10), (4, 30)]:
    for _ in range(count):
        squares.append(create_random_square(0.0, size=s))

running = True
while running:
    dt = clock.tick(FPS) / 1000.0
    elapsed_time += dt
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    eaten = set()
    for i, predator in enumerate(squares):
        for j, prey in enumerate(squares):
            if i != j and predator.size > prey.size and predator.check_collision(prey):
                eaten.add(j)
                predator.size = min(predator.size + 2, 50) 

    new_squares = []
    for i, s in enumerate(squares):
        if s.is_dead(elapsed_time) or i in eaten:
            new_squares.append(create_random_square(elapsed_time, size=s.size if i in eaten else None))
        else:
            new_squares.append(s)
    squares = new_squares

    screen.fill((30, 30, 30))
    for s in squares:
        s.update(squares, dt)
        s.check_boundaries(800, 600)
        s.draw(screen)

    pygame.display.flip()

pygame.quit()