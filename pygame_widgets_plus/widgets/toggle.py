from pygame_widgets_plus.widget import WidgetBase
from pygame_widgets_plus.widgets import Slider
from pygame_widgets_plus.mouse import MouseHandler, MouseState
from pygame_widgets_plus.helpers import input2Color

import pygame.draw

class Toggle(Slider):
    def __init__(self, surface, x, y, width, height, **kwargs):
        super().__init__(surface, x, y, width, height)
        self._barRect.height = height
        self._barRect.center = (x, y)
        self._barRectProgress.height = height
        self._barRectProgress.center = (x, y)

        self._physDist = self._barRect.right - self._barRect.left

        self._handleRadius = height // 2
        self._handleRect.width = self._handleRadius*2
        self._handleRect.height = self._handleRadius*2
        self._handleRect.center = self._calcPosFromValue()

    def _doesCollide(self, x, y):
        return WidgetBase._doesCollide(self, x, y)

    def update(self):        
        if self._doesCollide(MouseHandler.mouseX, MouseHandler.mouseY):
            if (MouseHandler.state == MouseState.MOUSEBUTTONDOWN):
                self.active = not self.active

        if self.active:
            if self._onMouseClicked:
                self._onMouseClicked(self._onMouseClickedArgs)

            self._handleRect.right = self._barRect.right
        else:
            self._handleRect.left = self._barRect.left
        
        self._barRectProgress.width = self._handleRect.centerx - self._barRectProgress.left
        self._barRectProgress.right = self._handleRect.centerx