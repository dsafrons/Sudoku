from Cell import Cell


class LegalChecker:
    def __init__(self):
        self.boxes = [[((xbox*3)+i-1, (ybox*3)+j-1) for j in range(1, 4) for i in range(1, 4)] for xbox in range(3) for ybox in range(3)]

    def boxes_legal(self, board, pos, num):
        board[pos[0]][pos[1]] = Cell(num, pos[0], pos[1], False)
        for box in self.boxes:
            nums_in_box_duplicates = []
            nums_in_box = set()
            for cell_coordinate in box:
                cell = board[cell_coordinate[0]][cell_coordinate[1]]
                if cell.value != 0:
                    nums_in_box_duplicates.append(cell.value)
                    nums_in_box.add(cell.value)

            if len(nums_in_box) != len(nums_in_box_duplicates):
                return False
        return True

    def rows_legal(self, board, pos, num):
        board[pos[0]][pos[1]] = Cell(num, pos[0], pos[1], False)
        for row in range(9):
            nums_in_row_duplicates = []
            nums_in_row = set()
            for col in range(9):
                cell = board[row][col]
                if cell.value != 0:
                    nums_in_row_duplicates.append(cell.value)
                    nums_in_row.add(cell.value)

            if len(nums_in_row_duplicates) != len(nums_in_row):
                return False
        return True

    def cols_legal(self, board, pos, num):
        board[pos[0]][pos[1]] = Cell(num, pos[0], pos[1], False)
        for col in range(9):
            nums_in_col_duplicates = []
            nums_in_col = set()
            for row in range(9):
                cell = board[row][col]
                if cell.value != 0:
                    nums_in_col_duplicates.append(cell.value)
                    nums_in_col.add(cell.value)

            if len(nums_in_col_duplicates) != len(nums_in_col):
                return False
        return True


    def check_board_legal(self, board, pos, num):
        return self.boxes_legal(board, pos, num) and self.rows_legal(board, pos, num) and self.cols_legal(board, pos, num)
