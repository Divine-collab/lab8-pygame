# Lab 8: Pygame Moving Squares Animation

A simple Python application using Pygame that displays 10 colored squares moving randomly on a canvas with size-based velocity scaling.

## Project Overview

This project demonstrates fundamental concepts in:
- **Object-Oriented Programming** - Square class encapsulation
- **Game Loop Architecture** - Event handling, update, render cycle
- **Boundary Detection** - Collision detection and bouncing
- **Mathematical Interpolation** - Linear scaling of velocity based on size
- **Pygame Graphics** - Drawing and animation

## Features

✨ **10 Random Colored Squares**
- Each square has a unique random color (RGB values 0-255)
- Varying sizes (10-40 pixels)
- Random initial positions on canvas

🚀 **Size-Based Velocity Scaling**
- Velocity directly proportional to square size
- Smaller squares move slower
- Larger squares move faster (inverted option available)
- Maximum speed capped at `MAX_SPEED = 5` pixels/frame

🎯 **Boundary Bouncing**
- Squares bounce off canvas edges
- Velocity reverses when hitting walls
- No squares escape the canvas

⚙️ **Configurable Parameters**
- `MIN_SIZE = 10` - Minimum square dimension
- `MAX_SIZE = 40` - Maximum square dimension
- `MAX_SPEED = 5` - Maximum velocity in pixels/frame
- `SCREEN_WIDTH = 800`, `SCREEN_HEIGHT = 600` - Canvas size
- `FPS = 60` - Frame rate

## Installation

### Prerequisites
- Python 3.7+
- Pygame 2.0+

### Setup
```bash
# Clone or navigate to the project directory
cd /Users/divinebyishimo/projects/AI4SE/lab8-pygame

# Create virtual environment (if not already created)
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install Pygame
pip install pygame
```

## Usage

Run the application:
```bash
python main.py
```

Or using the specific Python executable:
```bash
./.venv/bin/python main.py
```

**Close the window** to exit the application.

## Code Structure

### `Square` Class
Represents a moving square with the following methods:

- **`__init__(x, y, size, color, velocity_x, velocity_y)`** - Initialize square with position, size, color, and velocity
- **`update()`** - Move square by adding velocity to position
- **`draw(surface)`** - Render square on display surface
- **`check_boundaries(width, height)`** - Detect wall collisions and reverse velocity

### Game Loop
The main game loop runs at 60 FPS and performs:
1. **Event Handling** - Check for quit events
2. **Update Phase** - Move all squares and check boundaries
3. **Render Phase** - Clear screen and draw all squares
4. **Display Update** - Flip display to show changes

## Velocity Formulas

### Current Formula (Smaller = Faster - Inverse)
```python
speed = (MAX_SIZE - size) / (MAX_SIZE - MIN_SIZE) * MAX_SPEED
```
- Size 10px → speed 5 pixels/frame (fastest)
- Size 25px → speed 2.5 pixels/frame
- Size 40px → speed 0 pixels/frame (slowest)

### Alternative Formula (Larger = Faster - Linear)
```python
speed = (size - MIN_SIZE) / (MAX_SIZE - MIN_SIZE) * MAX_SPEED
```
- Size 10px → speed 0 pixels/frame (slowest)
- Size 25px → speed 2.5 pixels/frame
- Size 40px → speed 5 pixels/frame (fastest)

## Mathematical Concepts

### Linear Interpolation
The formula `(value - min) / (max - min)` normalizes any value to a 0-1 range.

**Example:**
```
(25 - 10) / (40 - 10) = 15 / 30 = 0.5
```

Multiplying by `MAX_SPEED` scales this ratio to the desired range:
```
0.5 * 5 = 2.5 pixels/frame
```

## Global Constants

| Constant | Value | Purpose |
|----------|-------|---------|
| `MIN_SIZE` | 10 | Minimum square size |
| `MAX_SIZE` | 40 | Maximum square size |
| `MAX_SPEED` | 5 | Maximum velocity cap |
| `SCREEN_WIDTH` | 800 | Canvas width |
| `SCREEN_HEIGHT` | 600 | Canvas height |
| `FPS` | 60 | Frame rate |

## Files

- `main.py` - Main application code
- `README.md` - This file
- `JOURNAL.md` - Development progress journal
- `.venv/` - Python virtual environment

## Learning Outcomes

After completing this project, you will understand:
- ✅ Object-oriented programming with Python classes
- ✅ Game loop architecture and patterns
- ✅ Collision detection and response
- ✅ Linear interpolation and mathematical scaling
- ✅ Pygame library basics (initialization, drawing, events, display)
- ✅ Why global constants improve code maintainability

## Future Enhancements

Possible improvements to extend this project:
- [ ] Mouse tracking - squares follow mouse cursor
- [ ] Collision detection between squares
- [ ] Sound effects on wall bounce
- [ ] Keyboard controls to spawn new squares
- [ ] Performance metrics display (FPS counter)
- [ ] Different shapes (circles, triangles)
- [ ] Gravity simulation
- [ ] Trail effects behind moving squares

## Author

Created as part of Lab 8 for AI4SE course.

## License

This project is open source and available for educational purposes.
