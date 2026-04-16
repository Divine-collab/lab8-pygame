# Code Explorer Guide

## Overview

`code-explorer.html` is an interactive, browser-based documentation tool for exploring the Pygame predator-prey simulation project.

## Features

### 7 Interactive Tabs

1. **Overview**
   - Project concept and description
   - Core features and learning outcomes
   - Behavioral effects visualization
   - Key statistics and metrics

2. **Architecture**
   - High-level system design
   - Data flow diagrams (Mermaid)
   - Class structure
   - Configuration constants reference

3. **Square Class**
   - Complete API documentation
   - Method signatures and parameters
   - Algorithm explanations
   - Code examples and walkthroughs

4. **Game Loop**
   - Initialization phase
   - Main loop structure
   - Event handling
   - Frame rate control (60 FPS)

5. **Configuration**
   - All configurable constants
   - Tuning guidelines
   - Impact of each parameter
   - How to adjust behavior

6. **Algorithms**
   - Detailed pseudocode
   - Vector mathematics breakdown
   - Step-by-step examples
   - Time complexity analysis

7. **Performance**
   - Computational complexity (O(n²))
   - Scaling implications
   - Frame time budget
   - Optimization opportunities

## How to Use

### Opening the Explorer

Simply open the file in any modern web browser:
```bash
# macOS
open code-explorer.html

# Linux
firefox code-explorer.html

# Or drag into your browser
```

### Navigation

- Click any tab button at the top to switch sections
- Scroll to view all content within a tab
- Click links to jump between related sections

### Responsive Design

The explorer is mobile-responsive:
- **Desktop (1000px+):** Two-column layouts for comparisons
- **Tablet/Mobile (<1000px):** Single-column layouts

## Content Structure

### Code Blocks
- Dark background with color-coded syntax
- Full pseudocode for algorithms
- Real-world examples with numbers

### Tables
- Reference for all constants
- Parameter documentation
- Scaling impact analysis

### Diagrams
- Mermaid flowcharts for system architecture
- Data flow visualization
- Update sequence diagrams

### Cards
- Organized information chunks
- Section headers with description
- Multiple visual hierarchy levels

## Key Sections to Explore

### For Understanding the Code
Start with:
1. **Overview** → Get the big picture
2. **Architecture** → Understand system design
3. **Square Class** → Learn the core logic

### For Implementation Details
Dive into:
1. **Algorithms** → How vectors and physics work
2. **Game Loop** → Frame-by-frame execution
3. **Performance** → Why design choices were made

### For Customization
Check:
1. **Configuration** → What each constant does
2. **Configuration** → Tuning guidelines
3. **Performance** → Scaling implications

## Browser Requirements

- Modern browser (Chrome, Firefox, Safari, Edge 2020+)
- JavaScript enabled
- Internet connection (for Mermaid diagram library via CDN)

## Offline Use

If offline or using without internet:
1. The page loads (CSS/structure work)
2. Mermaid diagrams won't render (but text explanations remain)
3. Download Mermaid locally to fix this

## Color Theme

Uses Catppuccin Mocha palette for readability:
- **Accent (Blue):** Primary highlights, titles
- **Green:** Methods and function names
- **Yellow:** Code and parameters
- **Cyan:** Important notes
- **Red:** Warnings/issues (if any)

## Educational Use

This explorer is designed for:
- **Learning:** Understand AI behavior, vector math, game loops
- **Teaching:** Share with students/teammates
- **Reference:** Quick lookup during development
- **Portfolio:** Professional documentation example

## File Size

- **52 KB** - Includes all content and styling
- No external dependencies (except Mermaid CDN for diagrams)
- Can be copied/shared as single file

## Updates

When code changes:
1. Update relevant algorithm sections
2. Update configuration constants
3. Recalculate performance metrics
4. Verify all examples still match code

## Questions?

Each section includes:
- Why (the reasoning)
- How (the mechanism)
- When (when to use)
- Impact (what changes if you modify)

---

**Last Updated:** 13 April 2026
**Project:** Lab 8 - Pygame Predator-Prey Simulation
