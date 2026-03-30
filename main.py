import pygame
import random
MIN_SIZE = 10
MAX_SIZE = 40
MAX_SPEED = 5


# ============================================================================
# STEP 1: Define the Square Class
# ============================================================================

class Square:
    """Represents a moving square on the canvas"""
    
    def __init__(self, x, y, size, color, velocity_x, velocity_y):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
    
    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
    
    def draw(self, surface):
        pygame.draw.rect(
            surface,
            self.color,
            pygame.Rect(self.x, self.y, self.size, self.size)
        )
    
    def check_boundaries(self, width, height):
        # Bounce on left/right walls
        if self.x < 0 or self.x + self.size > width:
            self.velocity_x *= -1
        
        # Bounce on top/bottom walls
        if self.y < 0 or self.y + self.size > height:
            self.velocity_y *= -1


# ============================================================================
# STEP 2: Initialize Pygame and Create Window
# ============================================================================

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Squares")

clock = pygame.time.Clock()


# ============================================================================
# STEP 3: Create 10 Random Squares
# ============================================================================

squares = []

for _ in range(100):
    size = random.randint(MIN_SIZE, MAX_SIZE)
    
    x = random.randint(0, SCREEN_WIDTH - size)
    y = random.randint(0, SCREEN_HEIGHT - size)
    
    color = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )
    
    # Calculate speed based on size (larger = faster)
    # Scale speed from 1 to MAX_SPEED based on size
    speed = (MAX_SIZE - size) / (MAX_SIZE - MIN_SIZE) * MAX_SPEED
    
    # Random direction for each velocity
    velocity_x = random.choice([-1, 1]) * speed
    velocity_y = random.choice([-1, 1]) * speed
    
    # Ensure we don't exceed MAX_SPEED
    if abs(velocity_x) > MAX_SPEED:
        velocity_x = MAX_SPEED if velocity_x > 0 else -MAX_SPEED
    if abs(velocity_y) > MAX_SPEED:
        velocity_y = MAX_SPEED if velocity_y > 0 else -MAX_SPEED

    square = Square(x, y, size, color, velocity_x, velocity_y)
    squares.append(square)


# ============================================================================
# STEP 4: Implement the Game Loop
# ============================================================================

running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update squares
    for square in squares:
        square.update()
        square.check_boundaries(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Clear screen (white)
    screen.fill((255, 255, 255))

    # Draw squares
    for square in squares:
        square.draw(screen)

    # Update display
    pygame.display.flip()

    # Control FPS
    clock.tick(60)


# ============================================================================
# STEP 5: Cleanup
# ============================================================================

pygame.quit()
# ============================================================================

pygame.quit()