# Lab 8 Pygame - Project Journal

## Project Overview
Building a simple Python application using Pygame that displays 10 colored squares moving randomly on a canvas.

## Iterations

### Iteration 1: Initial Setup & Planning
**Date:** 27 March 2026
**Status:** Completed

**Tasks:**
- [x] Analyzed project requirements
- [x] Explained project structure and approach
- [x] Created JOURNAL.md for progress tracking
- [x] Explained core concepts and approach
- [ ] Implement core Pygame application with Square class
- [ ] Create 10 random squares with movement
- [ ] Implement game loop and boundary handling

**Key Decisions:**
- Using Pygame for graphics and animation
- Will create a Square class to encapsulate square behavior
- Squares will bounce off canvas boundaries
- Random velocities for each square

**Next Steps:**
- Implement the main Pygame application
- Create Square class with position, velocity, size, and color
- Set up game loop with event handling and rendering

---

### Iteration 2: Core Implementation
**Date:** 27 March 2026 - 30 March 2026
**Status:** Completed

**Tasks:**
- [x] Implement Square class
- [x] Create Pygame window and initialization
- [x] Implement game loop with event handling
- [x] Add 10 random squares
- [x] Implement boundary collision detection
- [x] Test and debug

**Implementation Details:**
- Window size: 800x600 pixels
- FPS: 60 frames per second
- Boundary handling: Squares bounce off edges
- 10 squares with random sizes (20-50px), colors, positions, and velocities
- Pygame library successfully installed and application running

**Square Class Methods:**
- `__init__(x, y, size, color, velocity_x, velocity_y)`: Initializes square with all properties
- `update()`: Moves square by adding velocity to position each frame
- `draw(surface)`: Renders square on display surface using pygame.draw.rect()
- `check_boundaries(width, height)`: Detects wall collisions and reverses velocity for bouncing

**Game Loop Flow:**
1. Handle events (quit event)
2. Update all squares (move and check boundaries)
3. Clear screen with white background
4. Draw all squares at new positions
5. Update display (60 FPS)

---

### Iteration 3: Code Review & Documentation
**Date:** 30 March 2026
**Status:** Completed

**Tasks:**
- [x] Explained random square sizing using `random.randint(20, 50)`
- [x] Documented each function step-by-step
- [x] Explained complete animation cycle and game loop execution
- [x] Provided detailed function breakdowns with examples

**Key Learnings:**
- Each square updates 60 times per second
- Position updates accumulate: position += velocity each frame
- Boundary checking: uses `x < 0`, `x + size > width`, `y < 0`, `y + size > height`
- Bouncing: `velocity *= -1` reverses direction
- Game loop: handle events → update → clear → draw → display

---

### Iteration 4: Global Constants & Speed Scaling
**Date:** 30 March 2026
**Status:** Completed

**Tasks:**
- [x] Added global constants: MIN_SIZE, MAX_SIZE, MAX_SPEED
- [x] Explained why globals are defined at top of code
- [x] Implemented size-based velocity scaling
- [x] Explained linear interpolation formula: `(size - MIN_SIZE) / (MAX_SIZE - MIN_SIZE) * MAX_SPEED`
- [x] Explored inverse formula for smaller = faster behavior
- [x] Analyzed user's experimental changes to speed formula
- [x] Documented all speed formula variations

**Global Constants Used:**
- `MIN_SIZE = 10` (minimum square size in pixels)
- `MAX_SIZE = 40` (maximum square size in pixels)
- `MAX_SPEED = 5` (maximum velocity in pixels/frame)

**Why Define Globals at Top:**
- Easy to find and change one value
- Single source of truth (avoid duplicates)
- Makes code maintainable and self-documenting
- Enables quick configuration adjustments

**Speed Formulas Explored:**

1. **Original Linear (Larger = Faster):**
   - Formula: `(size - MIN_SIZE) / (MAX_SIZE - MIN_SIZE) * MAX_SPEED`
   - Result: Size 10→speed 0, Size 25→speed 2.5, Size 40→speed 5
   - Status: ✅ Correct - proportional scaling

2. **Multiplication (Non-linear, exponential growth):**
   - Formula: `(size - MIN_SIZE) * (MAX_SIZE - MIN_SIZE) * MAX_SPEED`
   - Result: Speeds become unrealistic (2250+)
   - Status: ❌ Broken - squares move off-screen instantly

3. **Division (Makes all speeds slow):**
   - Formula: `(size - MIN_SIZE) / (MAX_SIZE - MIN_SIZE) / MAX_SPEED`
   - Result: Size 10→speed 0, Size 25→speed 0.1, Size 40→speed 0.2
   - Status: ❌ Broken - all squares barely move

4. **Inverse (Smaller = Faster):**
   - Formula: `(MAX_SIZE - size) / (MAX_SIZE - MIN_SIZE) * MAX_SPEED`
   - Result: Size 10→speed 5, Size 25→speed 2.5, Size 40→speed 0
   - Status: ✅ Correct - inverse scaling

**Current Implementation Issues:**
- Loop still creates 100 squares instead of 10: `range(100)` should be `range(10)`
- Current speed formula uses division: `/MAX_SPEED` (slow speeds)

**Key Insights Learned:**
- Formula operators matter: `/` vs `*` creates completely different behaviors
- Linear interpolation: `(value - min) / (max - min)` normalizes to 0-1 ratio
- Multiplying by MAX_SPEED scales the ratio up to desired range
- Dividing by MAX_SPEED makes everything very slow
- Inverse relationships: swap `(size - MIN)` with `(MAX - size)`

---

## Development Log

### Notes
- Project location: `/Users/divinebyishimo/projects/AI4SE/lab8-pygame/`
- Main file: `main.py`
