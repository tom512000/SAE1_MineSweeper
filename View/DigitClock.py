# View/DigitClock.py
import pygame

from View.Digit import Digit
from View.images import Image


class DigitClock:

    def __init__(self, screen: pygame.Surface, pos: tuple, time: int = 0, off: bool = True):
        self.screen = screen
        self.pos = pos
        self.time = time
        self.off = off
        self.minutes = Digit(screen, pos, value=(time // 60) % 60, off=off)
        x, y = pos
        self.dots_x = x + 2*Image.get_digit_width()
        self.secondes = Digit(screen, ( self.dots_x + Image.get_digit_dots_width(), y),
                              value=time % 60, off=off)
        self.refresh()

    def refresh(self):
        self.screen.blit(Image.get_digit_dots_off() if self.off else Image.get_digit_dots(),
                         (self.dots_x, self.pos[1]))

    def set_on(self) -> bool:
        if self.off:
            self.off = False
            self.minutes.set_on()
            self.secondes.set_on()
            self.refresh()
            return True
        return False

    def set_off(self) -> bool:
        if not self.off:
            self.off = True
            self.minutes.set_off()
            self.secondes.set_off()
            self.refresh()
            return True
        return False

    def tick(self):
        self.time += 1
        self.minutes.set_value((self.time // 60) % 60)
        self.secondes.set_value(self.time % 60)

    def reset(self):
        self.time = 0
        self.minutes.set_value(0)
        self.secondes.set_value(0)
