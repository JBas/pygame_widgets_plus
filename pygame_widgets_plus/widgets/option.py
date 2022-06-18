from pygame_widgets_plus.widget import WidgetBase
from pygame_widgets_plus.mouse import MouseHandler, MouseState
from pygame_widgets_plus.helpers import input2Color

import pygame.draw


class Option(WidgetBase):

    def __init__(self, surface, x, y, size=10, style="square"):
        super().__init__(surface, x, y, size, size, isTopLevelParent=False)
        self._surface = surface

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
            pygame.draw.circle(self._surface, c, self._rect.center, self._rect.width//2)
        pygame.draw.circle(self._surface, c, self._rect.center, self._rect.width, width=3)

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