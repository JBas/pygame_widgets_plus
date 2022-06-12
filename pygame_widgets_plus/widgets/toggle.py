from pygame_widgets_plus.widgets import WidgetBase
from pygame_widgets_plus.mouse import MouseHandler, MouseState
from pygame_widgets_plus.helpers import input2Color

import pygame.draw

class Toggle(WidgetBase):
    def __init__(self, surface, x, y, width, height, **kwargs):
        super().__init__(surface, x, y, width, height,
                         kwargs.get("onMouseClicked", None), kwargs.get("onMouseClickedArgs", self),
                         kwargs.get("onMousePressed", None), kwargs.get("onMousePressedArgs", self),
                         kwargs.get("onMouseReleased", None), kwargs.get("onMouseReleasedArgs", self),
                         kwargs.get("onMouseMoved", None), kwargs.get("onMouseMovedArgs", self))

        self._active = False

    @property
    def active(self):
        return self._active

    def update(self):
        if self._doesCollide(MouseHandler.mouseX, MouseHandler.mouseY):
            if (MouseHandler.state == MouseState.MOUSEBUTTONDOWN):
                self._active = not self._active
        pass

    def draw(self):
        pass