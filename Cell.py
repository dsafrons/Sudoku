class Cell:
    def __init__(self, value, row, col, changeable):
        self.row = row
        self.col = col
        self.value = value
        self.changeable = changeable
        self.possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.possible_values.remove(value) if value in self.possible_values else self.possible_values
        self.boxes = [[((xbox*3)+i-1, (ybox*3)+j-1) for j in range(1, 4) for i in range(1, 4)] for xbox in range(3) for ybox in range(3)]

    def tuple_in_list(self, t, l):
        for value in l:
            if value[0] == t[0] and value[1] == t[1]:
                return True
        return False

    def find_nums_in_row(self, board):
        values = set()
        for cell in board[self.row]:
            if cell != self:
                values.add(cell.value)

        return values

    def find_nums_in_col(self, board):
        values = set()
        for row in range(9):
            cell = board[row][self.col]
            if cell != self:
                values.add(cell.value)

        return values

    def find_nums_in_box(self, board):
        values = set()
        for box in self.boxes:
            if self.tuple_in_list((self.row, self.col), box):
                for cell_coord in box:
                    if board[cell_coord[0]][cell_coord[1]] != self:
                        values.add(board[cell_coord[0]][cell_coord[1]].value)

        return values

    def update_possible_values(self, board):
        nums_cant_use = set()
        for num in self.find_nums_in_col(board):
            nums_cant_use.add(num)
        for num in self.find_nums_in_box(board):
            nums_cant_use.add(num)
        for num in self.find_nums_in_row(board):
            nums_cant_use.add(num)

        nums_total = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for num in nums_cant_use:
            nums_total.remove(num)

        nums_total.remove(self.value) if self.value in nums_total else nums_total
        self.possible_values = nums_total
