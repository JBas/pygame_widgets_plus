from pygame_widgets_plus.widget import WidgetBase
from pygame_widgets_plus.mouse import MouseHandler, MouseState
from pygame_widgets_plus.helpers import input2Color

import pygame.draw

class Slider(WidgetBase):
    def __init__(self, surface, x, y, width, height, **kwargs):
        super().__init__(surface, x, y, width, height,
                         kwargs.get("onMouseClicked", None), kwargs.get("onMouseClickedArgs", self),
                         kwargs.get("onMousePressed", None), kwargs.get("onMousePressedArgs", self),
                         kwargs.get("onMouseReleased", None), kwargs.get("onMouseReleasedArgs", self),
                         kwargs.get("onMouseMoved", None), kwargs.get("onMouseMovedArgs", self))

        self._min = kwargs.get("min", 0)
        self._max = kwargs.get("max", 10)
        self._value = kwargs.get("value", 5)

        
        self._rect.center = (x, y)

        self._handleRadius = height // 4
        self._handleRect = pygame.Rect(x, y, self._handleRadius*2, self._handleRadius*2)
        self._handleRect.center = (x, y)

        self._barRect = pygame.Rect(x, y, width, height//4)
        self._barRect.center = (x, y)
        self._active = False

        self._physDist = self._barRect.right - self._barRect.left

    def _doesCollide(self, x, y):
        return self._handleRect.collidepoint(x, y)

    def calculateValue(self):
        d = (self._physDist - self._handleRect.centerx)
        return

    def update(self):
        if self._doesCollide(MouseHandler.mouseX, MouseHandler.mouseY):
            if (MouseHandler.state == MouseState.MOUSEBUTTONDOWN):
                self._active = True
        if (MouseHandler.state == MouseState.MOUSEBUTTONUP):
                self._active = False
            
        if self._active:       
            if MouseHandler.mouseX >= self._barRect.right:
                self._handleRect.centerx = self._barRect.right
            elif MouseHandler.mouseX <= self._barRect.left:
                self._handleRect.centerx = self._barRect.left
            else:
                self._handleRect.centerx = MouseHandler.mouseX

    def draw(self):
        pygame.draw.rect(self._surface, (100, 100, 100), self._barRect, border_radius=20)
        pygame.draw.circle(self._surface, (150, 150, 150), self._handleRect.center, self._handleRadius)
        pass