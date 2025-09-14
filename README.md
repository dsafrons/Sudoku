# Sudoku

A Sudoku solver and generator implemented in Python.  
The project uses object-oriented design with dedicated classes for cells, boards, rule checking, and solving.

## Features

- **Board generation** (`BoardGenerator.py`) – builds a new Sudoku grid  
- **Cell representation** (`Cell.py`) – object for each square with value and candidates  
- **Rule checking** (`LegalChecker.py`) – validates moves against Sudoku rules  
- **Solver** (`SudokuSolver.py`) – backtracking algorithm to solve puzzles  
- **Main entry point** (`Sudoku.py`) – runs the program

## How it Works
- Each Cell stores a value (or blank) and possible candidates.
- LegalChecker ensures rows, columns, and subgrids follow Sudoku rules.
- SudokuSolver attempts to solve puzzles by trying candidates and backtracking when invalid.
- BoardGenerator can create random boards that can be fed into the solver.

## Project Structure
```
Sudoku/
├── BoardGenerator.py   # Generates Sudoku boards
├── Cell.py             # Cell object with value/candidates
├── LegalChecker.py     # Validity checks for moves
├── Sudoku.py           # Main entry point
├── SudokuSolver.py     # Backtracking solver
├── font.ttf            # Font file (used for display)
└── .idea/              # IDE config (can be ignored)
```
