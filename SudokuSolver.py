from LegalChecker import LegalChecker
from random import shuffle


class Solver:
    def __init__(self):
        self.sudoku_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.legal_checker = LegalChecker()
        self.counter = 0

    def board_full(self, board):
        for row in range(0, 9):
            for col in range(0, 9):
                if board[row][col].value == 0:
                    return False
        return True

    def fill_empty(self, board):
        for i in range(0, 81):
            row = i // 9
            col = i % 9
            if board[row][col].value == 0:
                shuffle(self.sudoku_nums)
                for value in self.sudoku_nums:
                    if self.legal_checker.check_board_legal(board, (row, col), value):
                        board[row][col].value = value
                        if self.board_full(board):
                            return True, board
                        else:
                            if self.fill_empty(board):
                                return True, board

                break
        board[row][col].value = 0

    def solve(self, board):
        for i in range(0, 81):
            row = i // 9
            col = i % 9
            if board[row][col].value == 0:
                for value in range(1, 10):
                    if self.legal_checker.check_board_legal(board, (row, col), value):
                        board[row][col].value = value
                        if self.board_full(board):
                            self.counter += 1
                            break
                        else:
                            if self.solve(board):
                                return True
                break
        board[row][col].value = 0
