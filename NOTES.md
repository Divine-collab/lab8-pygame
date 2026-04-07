# Lab 8 Pygame - Study Notes

## Core Concepts

### 1. Game Loop Architecture
The fundamental pattern used in all games and animations:
```
while running:
    handle_events()      # Process user input and system events
    update()            # Update game state (positions, collisions)
    render()            # Draw everything on screen
    control_fps()       # Maintain consistent frame rate
```

### 2. Object-Oriented Programming

#### Classes Encapsulate Behavior
- Group related data and methods together
- `Square` class encapsulates: position, size, color, velocity, movement logic
- Methods: `__init__()`, `update()`, `draw()`, `check_boundaries()`

#### Why Use Classes?
- ✅ Easier to create multiple similar objects (100 squares)
- ✅ Code organization and readability
- ✅ Easy to extend with new features
- ✅ Separation of concerns

### 3. Position and Velocity

#### Position: (x, y) coordinates
- `x` = horizontal position (0 = left edge, 800 = right edge)
- `y` = vertical position (0 = top edge, 600 = bottom edge)

#### Velocity: Rate of change
- `velocity_x` = pixels moved per frame horizontally
- `velocity_y` = pixels moved per frame vertically
- `velocity += direction` determines if positive (→ or ↓) or negative (← or ↑)

#### Update Formula
```python
x += velocity_x
y += velocity_y
```
Repeated 60 times/second creates smooth animation.

### 4. Boundary Detection and Bouncing

#### Collision Detection
```python
# Left/Right walls
if x < 0:                    # Hit left wall
    velocity_x *= -1        # Bounce right
if x + size > width:         # Hit right wall
    velocity_x *= -1        # Bounce left

# Top/Bottom walls
if y < 0:                    # Hit top wall
    velocity_y *= -1        # Bounce down
if y + size > height:        # Hit bottom wall
    velocity_y *= -1        # Bounce up
```

#### Why `velocity *= -1`?
- Changes direction without changing speed magnitude
- If moving right at +3 → becomes -3 (moves left)
- If moving down at +2 → becomes -2 (moves up)

### 5. Mathematical Scaling (Linear Interpolation)

#### Formula Structure
```
normalized_value = (current - min) / (max - min)
scaled_value = normalized_value * scale_factor
```

#### Example with Speed Scaling
```
speed = (size - MIN_SIZE) / (MAX_SIZE - MIN_SIZE) * MAX_SPEED
```

**Step-by-step for size=25:**
1. `(25 - 10) = 15` (distance from minimum)
2. `(40 - 10) = 30` (total range)
3. `15 / 30 = 0.5` (normalized ratio, 0 to 1)
4. `0.5 * 5 = 2.5` (scaled to MAX_SPEED range)

#### Use Cases
- Fade effects (0 to 255 opacity)
- Audio volume control
- Color gradients
- Speed scaling based on size/level

### 6. Global Constants

#### Why Define at Top?
```python
# ✅ GOOD - Easy to find and change
MIN_SIZE = 10
MAX_SIZE = 40
MAX_SPEED = 5

# ❌ BAD - Scattered throughout code
size = random.randint(10, 40)
speed = ... * 5
```

#### Benefits
- **Maintainability:** Change one value, affects entire program
- **Self-documenting:** Constants describe program configuration
- **Testability:** Easy to test different values
- **DRY Principle:** Don't Repeat Yourself

### 7. Pygame Fundamentals

#### Initialization
```python
pygame.init()  # Must call first before using pygame
```

#### Display Setup
```python
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Title")
```

#### Event Handling
```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:  # User clicked close
        running = False
```

#### Drawing
```python
pygame.draw.rect(surface, color, pygame.Rect(x, y, width, height))
```

#### Display Update
```python
pygame.display.flip()  # Show all changes
```

#### Frame Rate Control
```python
clock = pygame.time.Clock()
clock.tick(60)  # Maximum 60 FPS
```

## Common Mistakes to Avoid

### ❌ Using `*` instead of `/` in formula
```python
speed = (size - MIN) * (MAX - MIN) * MAX_SPEED  # Wrong! Creates huge speeds
speed = (size - MIN) / (MAX - MIN) * MAX_SPEED  # Correct
```

### ❌ Forgetting to divide by range
```python
speed = (size - MIN) * MAX_SPEED  # Wrong! Not normalized
speed = (size - MIN) / (MAX - MIN) * MAX_SPEED  # Correct
```

### ❌ Creating objects outside loop
```python
# Wrong - only creates 1 square
square = Square(...)
squares.append(square)

# Correct - creates 10 squares
for _ in range(10):
    square = Square(...)
    squares.append(square)
```

### ❌ Forgetting pygame.quit()
```python
# Wrong - leaves resources open
# program ends without cleanup

# Correct
pygame.quit()
```

### ❌ Not calling update() in game loop
```python
# Wrong - squares don't move
for square in squares:
    square.draw(screen)

# Correct
for square in squares:
    square.update()  # Move first
    square.draw(screen)
```

## Formulas Reference

### Speed Scaling Formulas

#### 1. Larger = Faster (Linear)
```
speed = (size - MIN) / (MAX - MIN) * MAX_SPEED
```
- Small → slow
- Large → fast

#### 2. Smaller = Faster (Inverse)
```
speed = (MAX - size) / (MAX - MIN) * MAX_SPEED
```
- Small → fast
- Large → slow

#### 3. Exponential (Non-linear)
```
speed = (size - MIN) * (MAX - MIN) * MAX_SPEED
```
- ⚠️ Creates unrealistic speeds
- Not recommended

### Boundary Detection
```
left_edge = 0
right_edge = SCREEN_WIDTH
top_edge = 0
bottom_edge = SCREEN_HEIGHT

square_left = x
square_right = x + size
square_top = y
square_bottom = y + size
```

## Key Takeaways

1. **Game loops** drive animation - update positions, then redraw
2. **Classes** organize code - Square encapsulates all square behavior
3. **Velocity** is rate of change - determines how fast objects move
4. **Interpolation** scales values - from min/max to desired range
5. **Pygame** is a graphics library - handles drawing and events
6. **Constants** improve code - make values easy to find and change
7. **Operators matter** - `/` vs `*` produces completely different results

## Debugging Tips

### If squares don't move:
- Check `velocity_x` and `velocity_y` are not zero
- Verify `update()` is being called in game loop
- Check velocity calculation formula

### If squares move too fast:
- Reduce `MAX_SPEED` constant
- Check velocity formula (avoid multiplication in denominator)
- Verify division is used, not multiplication

### If squares disappear:
- Check boundary detection logic
- Verify `x` and `y` stay within screen bounds
- Check bouncing reverses velocity correctly

### If only some squares appear:
- Check loop creates correct number of squares
- Verify all squares are being drawn
- Check no squares have invalid positions

## Practice Exercises

1. **Change Colors:**
   - Make all squares the same color
   - Use a color gradient based on size

2. **Change Sizes:**
   - Set MIN_SIZE = 5, MAX_SIZE = 60
   - Make all squares same size

3. **Change Speed:**
   - Try different speed formulas
   - Add acceleration/deceleration

4. **Add Features:**
   - Count frames and display FPS
   - Print square positions to console
   - Add a reset key to restart

5. **Explore Physics:**
   - Add gravity (y velocity increases each frame)
   - Add damping (velocity decreases slightly each bounce)
   - Add friction (velocity slows down over time)

6. **My Thinking on Flee AI Behavior**

**Core Concept:**
Smaller squares detect larger squares nearby and flee away from them, while larger squares continue wandering without changing behavior. This creates a "predator-prey" dynamic.

**Detailed Mechanics:**

1. **Distance Detection:**
   - Small squares calculate distance to all other squares
   - Formula: `distance = sqrt((other.x - self.x)² + (other.y - self.y)²)`
   - Only react if distance < DETECTION_RANGE (e.g., 100 pixels)

2. **Threat Identification:**
   - Only larger squares (larger by SIZE_THRESHOLD) trigger flee
   - Larger squares are passive obstacles
   - All intelligence is in the small squares

3. **Speed Response (Distance-Based Force):**
   - Closer threat → faster flee response
   - `force = (DETECTION_RANGE - distance) / DETECTION_RANGE`
   - At 0 distance (touching): force = 1.0 (maximum panic)
   - At 100px distance: force = 0.0 (safe, stop fleeing)
   - At 50px distance: force = 0.5 (moderate fear)

4. **Direction Calculation:**
   - Calculate vector AWAY from threat
   - `flee_x = self.x - threat.x`
   - `flee_y = self.y - threat.y`
   - This gives the escape direction

5. **Directional Randomness (±60° Rotation):**
   - Flee direction isn't rigid
   - Can rotate by ±60° clockwise or anticlockwise
   - Prevents predictable straight-line fleeing
   - Maintains chaotic, organic movement

6. **Minimum Safe Distance:**
   - DETECTION_RANGE defines awareness boundary
   - Threat detection stops beyond this range
   - Prevents infinite chase loops
   - Allows squares to feel "safe" when far enough

7. **Interaction with Jitter:**
   - First: Calculate and apply flee response
   - Then: Apply existing jitter (±30° randomness)
   - Result: Panicked but erratic movement
   - Not predictable, but clearly intentional

**Configuration Parameters Needed:**
```python
DETECTION_RANGE = 100       # How far ahead squares "see"
SIZE_THRESHOLD = 5          # Minimum size difference to trigger flee
FLEE_FORCE = 2.0            # Strength of panic response
FLEE_ANGLE_VARIANCE = 60    # ±60° directional randomness in flee
```

**Algorithm Summary:**
```
For each small square per frame:
  1. Detect all squares larger than (self.size + SIZE_THRESHOLD)
  2. For each threat within DETECTION_RANGE:
     - Calculate distance and force (closer = stronger)
     - Calculate flee direction (away vector)
     - Apply force × direction to velocity
  3. Combine all threat responses
  4. Apply jitter for final randomness
  5. Clamp velocity to MAX_SPEED
  6. Update position
```

**Expected Visual Effects:**
- Small squares cluster away from large ones
- Creates flowing, swirling escape patterns
- Adds sense of "intelligence" to movement
- Maintains unpredictability (not boring AI)
- More engaging animation than pure randomness
   - 


## Resources

- [Pygame Documentation](https://www.pygame.org/docs/)
- [Python Classes Tutorial](https://docs.python.org/3/tutorial/classes.html)
- [Game Loop Pattern](https://en.wikipedia.org/wiki/Game_loop)
- [Linear Interpolation](https://en.wikipedia.org/wiki/Linear_interpolation)
