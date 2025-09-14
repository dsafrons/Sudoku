from SudokuSolver import Solver
from Cell import Cell
from random import randint


class Board:
    def __init__(self, difficulty):
        # create empty grid
        self.board = [[Cell(0, row, col, False) for col in range(9)] for row in range(9)]
        self.solver = Solver()

        self.fill_empty_board()

        self.poke_holes(difficulty)

    def fix_changeable(self, board):
        for row in board:
            for cell in row:
                if cell.value == 0:
                    cell.changeable = True

    def fill_empty_board(self):
        self.board = self.solver.fill_empty(self.board)
        board = self.board[1]
        self.board = board

    def poke_holes(self, attempts):
        attempts = attempts
        self.solver.counter = 1

        while attempts > 0:
            row = randint(0, 8)
            col = randint(0, 8)
            while self.board[row][col].value == 0:
                row = randint(0, 8)
                col = randint(0, 8)

            backup = self.board[row][col]
            self.board[row][col].value = 0

            copy_grid = []
            for r in range(0, 9):
                copy_grid.append([])
                for c in range(0, 9):
                    copy_grid[r].append(self.board[r][c])

            self.solver.counter = 0
            self.solver.solve(copy_grid)

            if self.solver.counter != 1:
                self.board[row][col] = backup
                attempts -= 1
