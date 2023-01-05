import pygame
from View.images import Image
from View.Button import Button
from View.Digit import Digit
from View.DigitClock import DigitClock
from Controller.Controller import Controller

from Model.Constantes import *


UEVENT_CLOCK = pygame.USEREVENT + 1

class MineSweeper:
    def __init__(self, controller: Controller, nlines: int, ncolumns: int):
        self.nlines = nlines
        self.ncolumn = ncolumns

        MARGE = Image.get_margin()
        # Largeur de la fenêtre
        WIN_WIDTH = 2 * MARGE + ncolumns * Image.get_cell_width()
        # Hauteur de la fenêtre
        WIN_HEIGHT = 3 * MARGE + Image.get_button_height() + nlines * Image.get_cell_height()

        screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(0, 0, WIN_WIDTH, WIN_HEIGHT))

        self.controller = controller
        img = Image.get_btn_play()
        w = (WIN_WIDTH - img.get_width()) // 2
        btn_play = Button(screen, (w, MARGE), [Image.get_btn_play(), Image.get_btn_down()],
                          onClicked=self.controller.on_play)

        self.mines_count = Digit(screen, (WIN_WIDTH - MARGE - 2*Image.get_digit_width(), MARGE), off=True)
        self.clock = DigitClock(screen, (MARGE, MARGE), off=True)

        cell = Button(screen, (0, 0), [Image.get_cell_up(), Image.get_cell_down(), Image.get_cell_over()],
                      visible=False, onClicked=self.controller.on_clicked,
                      onPressed=self.controller.on_pressed, onReleased=self.controller.on_released)
        w, h = cell.get_width(), cell.get_height()
        y = 2 * MARGE + Image.get_button_height()
        self.cells = [btn_play]
        for i in range(nlines):
            x = MARGE
            for j in range(ncolumns):
                self.cells.append(cell.copy_to((x, y), params=(i, j)))
                x += w
            y += h

        self.refresh = False
        pygame.display.flip()

    def start_clock(self):
        pygame.time.set_timer(UEVENT_CLOCK, 1000)
        self.clock.set_on()
        self.clock.reset()

    def stop_clock(self):
        pygame.time.set_timer(UEVENT_CLOCK, 0)
        # self.clock.set_off()

    def mouse_button_down(self,  pos: tuple, button: int, touch: int) -> bool:
        res = False
        for c in self.cells:
            res = c.mouse_button_down(pos, button, touch) or res
        return res

    def mouse_button_up(self,  pos: tuple, button: int, touch: int) -> bool:
        res = False
        for c in self.cells:
            res = c.mouse_button_up(pos, button, touch) or res
        return res

    def mouse_move(self,  pos: tuple, button: int, touch: int) -> bool:
        res = False
        for c in self.cells:
            res = c.mouse_move(pos, button, touch) or res
        return res

    def play(self):
        while True:
            self.refresh = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.refresh = self.mouse_button_down(event.pos, event.button, event.touch) or self.refresh
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.refresh = self.mouse_button_up(event.pos, event.button, event.touch) or self.refresh
                elif event.type == pygame.MOUSEMOTION:
                    self.refresh = self.mouse_move(event.pos, event.buttons, event.touch) or self.refresh
                elif event.type == UEVENT_CLOCK:
                    self.clock.tick()
                    self.refresh = True
            if self.refresh:
                pygame.display.flip()

    def is_guessing(self):
        self.cells[0].set_image_up(Image.get_btn_guess())
        self.refresh = True

    def guessing_done(self):
        self.cells[0].set_image_up(Image.get_btn_play())
        self.refresh = True

    def get_index(self, pos: tuple) -> int:
        return pos[0]*self.ncolumn + pos[1] + 1

    def set_state(self, pos: tuple, n: int):
        if n == const.ID_MINE:
            self.set_mine(pos)
        else:
            self.cells[self.get_index(pos)].set_state(n)

        self.refresh = True

    def set_flag(self, pos: tuple):
        self.cells[self.get_index(pos)].set_flag()
        self.refresh = True

    def set_doubt(self, pos: tuple):
        self.cells[self.get_index(pos)].set_doubt()
        self.refresh = True

    def set_none(self, pos: tuple):
        self.cells[self.get_index(pos)].set_none()
        self.refresh = True

    def set_mine(self, pos: tuple):
        self.cells[self.get_index(pos)].set_mine()
        self.cells[0].set_image_up(Image.get_btn_loose())
        self.refresh = True

    def set_won(self):
        self.cells[0].set_image_up(Image.get_btn_win())
        self.refresh = True

    def reset(self):
        self.cells[0].set_image_up(Image.get_btn_up())
        for i in range(1, len(self.cells)):
            self.cells[i].set_none()
        self.clock.reset()
        pygame.display.flip()

    def set_mines_count(self, n: int) -> None:
        if self.mines_count.set_value(n):
            self.mines_count.set_on()
            self.refresh = True
