# Sudoku (Python + PyGame)

A playable Sudoku game with puzzle generation and solving, implemented in Python with **object-oriented design**.  
It uses **PyGame** for the graphical interface and separates responsibilities into dedicated classes for cells, boards, rule checking, and solving.

## Features

- **Board generation** (`BoardGenerator.py`)  
  - Creates a valid solved Sudoku board  
  - Removes numbers according to a difficulty setting  
- **Cell representation** (`Cell.py`)  
  - Each cell tracks its row, column, value, changeability, and possible values  
- **Rule checking** (`LegalChecker.py`)  
  - Ensures no duplicate numbers appear in any row, column, or 3×3 subgrid  
- **Solver** (`SudokuSolver.py`)  
  - Backtracking algorithm to fill in empty cells  
  - Used for both solving and verifying generated boards  
- **Main Game** (`Sudoku.py`)  
  - PyGame window with font rendering (`font.ttf`)  
  - Displays the board and allows user interaction  
  - Integrates generator, solver, and legality checks

## Requirements

- Python 3.8+
- [pygame](https://pypi.org/project/pygame/)

Install with:
```
pip install pygame
```

## Project Structure
```
Sudoku/
├── Sudoku.py          # Main entry point (PyGame window + game loop)
├── BoardGenerator.py  # Board class: generates full grid, removes values by difficulty
├── Cell.py            # Cell class: represents a Sudoku cell
├── LegalChecker.py    # Ensures moves comply with Sudoku rules
├── SudokuSolver.py    # Solver class: backtracking algorithm
├── font.ttf           # Font file used for rendering numbers
└── README.md
```

## How it Works

**1. Generation**

- A full board is created, then “holes” are poked according to difficulty.

**2. Gameplay**

- The board is drawn in PyGame, each cell rendered with `font.ttf`.
- The user can attempt to fill in values interactively (via input).

**3. Validation**

- The `LegalChecker` ensures new numbers don’t break Sudoku rules.

**4. Solving**

- The `Solver` can complete any valid puzzle using recursive backtracking.

## Future Improvements

- Difficulty selector for generation (rather than manual code input)
- Highlight conflicts and hints
- Timer and scoring system
- Export puzzles and solutions to text or image files
