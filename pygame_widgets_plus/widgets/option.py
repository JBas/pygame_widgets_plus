from pygame_widgets_plus.mouse import MouseHandler, MouseState
from pygame_widgets_plus.helpers import input2Color

import pygame.draw


class Option():

    def __init__(self, surface, x, y, size=10, style="square"):
        self._surface = surface
        self._x = y
        self._y = y
        self._size = size

        self._rect = pygame.Rect(0, 0, size, size)
        self._rect.center = (x, y)

        self._active = False

        self._style = style
        pass

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, a):
        self._active = a

    def doesCollide(self, x, y):
        return self._rect.collidepoint(x, y)

    def update(self):
        pass

    def drawCircle(self):
        c = (100, 100, 100)
        if (self.active):
            c = (0, 0, 240)
            pygame.draw.circle(self._surface, c, self._rect.center, self._size//2)
        pygame.draw.circle(self._surface, c, self._rect.center, self._size, width=3)

    def drawSquare(self):
        c = (100, 100, 100)
        if (self.active):
            c = (0, 0, 240)
            pygame.draw.rect(self._surface, c, self._rect, border_radius=3)
        pygame.draw.rect(self._surface, c, self._rect.inflate(self._rect.width, self._rect.height), width=3, border_radius=3)

    def draw(self):
        if (self._style == "circle"):
            self.drawCircle()
        else:
            self.drawSquare()