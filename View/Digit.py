# View/Digit.py
import pygame
from View.images import Image


class Digit:

    def __init__(self, screen: pygame.Surface, pos: tuple, n: int = 2, value: int = 0, off: bool = False):
        self.nb = n  # Nombre de digits à utiliser pour afficher le nombre
        self.pos = pos
        self.value = value
        self.screen = screen
        self.off = off
        self.refresh()

    def set_value(self, v: int) -> bool:
        if v != self.value:
            self.value = v
            self.refresh()
            return True
        return False

    def get_value(self) -> int:
        return self.value

    def set_on(self) -> bool:
        if self.off:
            self.off = False
            self.refresh()
            return True
        return False

    def set_off(self):
        if not self.off:
            self.off = True
            self.refresh()
            return True
        return False

    def refresh(self):
        x, y = self.pos
        w = Image.get_digit_width()
        x += (self.nb - 1)*w
        if self.off:
            for _ in range(self.nb):
                self.screen.blit(Image.get_digit_off(), (x, y))
                x -= w
        else:
            v = self.value
            for _ in range(self.nb):
                self.screen.blit(Image.get_digit(v % 10), (x, y))
                x -= w
                v //= 10

