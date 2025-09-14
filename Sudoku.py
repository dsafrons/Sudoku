import pygame
from sys import exit
from BoardGenerator import Board


class Sudoku:
    def __init__(self, display_surface, clock):
        # game setup from main
        self.display_surface = display_surface
        self.clock = clock

        # font
        self.font = pygame.font.Font('font.ttf', 60)

        # get unsolved board
        self.grid_generator = Board(4)
        self.board = self.grid_generator.board
        self.grid_generator.fix_changeable(self.board)
        self.update_all_cells_possibilities()

        # game functions
        self.selected = None

    def draw_lines(self):
        size = self.display_surface.get_width()
        # border lines
        border_line_width = 8
        pygame.draw.line(self.display_surface, 'black', (0, 0), (size, 0), border_line_width)
        pygame.draw.line(self.display_surface, 'black', (0, 0), (0, size), border_line_width)
        pygame.draw.line(self.display_surface, 'black', (0, size), (size, size), 7)
        pygame.draw.line(self.display_surface, 'black', (size-2, 0), (size-2, size), border_line_width)

        # inner lines(inc. thick box lines)
        # vertical
        for i in range(8):
            if i == 2 or i == 5:
                x_pos = ((size/3)*(0 if i == 2 else 1))+(size/3)
                pygame.draw.line(self.display_surface, 'black', (x_pos, 0), (x_pos, size), border_line_width-2)
            else:
                x_pos = ((size/9)*i)+(size/9)
                pygame.draw.line(self.display_surface, 'black', (x_pos, 0), (x_pos, size), border_line_width - 6)

        # horizontal
        for i in range(8):
            if i == 2 or i == 5:
                y_pos = ((size/3)*(0 if i == 2 else 1))+(size/3)
                pygame.draw.line(self.display_surface, 'black', (0, y_pos), (size, y_pos), border_line_width-2)
            else:
                y_pos = ((size/9)*i)+(size/9)
                pygame.draw.line(self.display_surface, 'black', (0, y_pos), (size, y_pos), border_line_width - 6)

    def update_all_cells_possibilities(self):
        for row in self.board:
            for cell in row:
                if cell.changeable:
                    cell.update_possible_values(self.board)

    def draw_nums(self):
        for row_index, row in enumerate(self.board):
            for cell_index, cell in enumerate(row):
                if cell.value != 0:
                    color = (100, 100, 100) if cell.changeable else 'black'
                    text = self.font.render(f'{cell.value}', True, color)
                    text_rect = text.get_rect()
                    text_rect.center = ((cell_index*(self.display_surface.get_width()/9))+(self.display_surface.get_width()/18), (row_index*(self.display_surface.get_width()/9))+(self.display_surface.get_width()/18))
                    self.display_surface.blit(text, text_rect)

    def update_selection(self, ev):
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = (int(pos[1]//(self.display_surface.get_width()/9)), int(pos[0]//(self.display_surface.get_width()/9)))
                if clicked[0] <= 8 and clicked[1] <= 8:
                    cell = self.board[clicked[0]][clicked[1]]

                    if cell.changeable:
                        if not self.selected:
                            self.selected = clicked
                        else:
                            if self.selected != clicked:
                                self.selected = clicked
                            else:
                                self.selected = None

    def draw_selected_square(self):
        if self.selected:
            x_center = (self.selected[1] * (self.display_surface.get_width()/9))
            y_center = (self.selected[0] * (self.display_surface.get_width()/9))
            pygame.draw.rect(self.display_surface, (130, 130, 130), pygame.Rect(x_center+2, y_center+2, self.display_surface.get_width()/9-1, self.display_surface.get_width()/9-1), 5, border_radius=9)

    def draw_buttons_based_off_selected(self):
        if self.selected:
            for i in range(1, 10):
                # if i in self.board[self.selected[0]][self.selected[1]].possible_values:
                x_center = ((i-1) * (self.display_surface.get_width()/9))
                y_center = 800
                pygame.draw.rect(self.display_surface, (60, 60, 60), pygame.Rect(x_center + 1, y_center + 8, self.display_surface.get_width() / 9 - 1, self.display_surface.get_width() / 9 - 1), 5, border_radius=9)

                text = self.font.render(f'{i}', True, (30, 30, 30))
                text_rect = text.get_rect()
                text_rect.center = (x_center + self.display_surface.get_width()/18, y_center + 6 + self.display_surface.get_width()/18)
                self.display_surface.blit(text, text_rect)

    def place_clicked_num(self, ev):
        if self.selected:
            for event in ev:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[1] >= self.display_surface.get_width():
                        number_clicked = int((pygame.mouse.get_pos()[0]//(self.display_surface.get_width()/9))+1)
                        # if number_clicked in self.board[self.selected[0]][self.selected[1]].possible_values:
                        self.board[self.selected[0]][self.selected[1]].value = number_clicked
                        self.update_all_cells_possibilities()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.board[self.selected[0]][self.selected[1]].value = 0
                        self.update_all_cells_possibilities()

    def draw_highlight_on_nums(self):
        if self.selected and pygame.mouse.get_focused():
            if pygame.mouse.get_pos()[1] >= self.display_surface.get_width():
                number_clicked = int((pygame.mouse.get_pos()[0] // (self.display_surface.get_width() / 9)) + 1)
                x_center = ((number_clicked - 1) * (self.display_surface.get_width() / 9))
                y_center = 800
                color = (115, 128, 144) if pygame.mouse.get_pressed()[0] else (188, 210, 238)
                pygame.draw.rect(self.display_surface, color, pygame.Rect(x_center + 1, y_center + 8, self.display_surface.get_width() / 9 - 1, self.display_surface.get_width() / 9 - 1), border_radius=9)

    def check_win(self):
        for row in self.board:
            for cell in row:
                if cell.value == 0:
                    return False
        return self.grid_generator.solver.legal_checker.check_board_legal(self.board, (0, 0), self.board[0][0].value)


    def update(self, event):
        # game logic updates
        self.update_selection(event)
        self.place_clicked_num(event)
        print('win') if self.check_win() else False

        # game renders
        self.display_surface.fill('white')
        self.draw_lines()
        self.draw_nums()
        self.draw_selected_square()
        self.draw_highlight_on_nums()
        self.draw_buttons_based_off_selected()


class Main:
    def __init__(self):
        # pygame inits
        pygame.init()
        self.display_surface = pygame.display.set_mode((800, 900))
        self.clock = pygame.time.Clock()

        # game initialization
        self.sudoku = Sudoku(self.display_surface, self.clock)

    def run(self):
        while True:
            ev = pygame.event.get()
            for event in ev:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.sudoku.update(ev)

            pygame.display.update()


if __name__ == '__main__':
    main = Main()
    main.run()
