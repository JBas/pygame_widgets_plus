from pygame_widgets_plus.widget import WidgetBase
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

        self._activeColor = input2Color(kwargs.get("activeColor", "blue"))
        self._inActiveColor = input2Color(kwargs.get("activeColor", "grey"))

    @property
    def active(self):
        return self._active

    def update(self):
        if self._doesCollide(MouseHandler.mouseX, MouseHandler.mouseY):
            if (MouseHandler.state == MouseState.MOUSECLICK):
                self._active = not self._active
                print("whut")
        pass

    def _drawHandle(self, c):
        pygame.draw.circle(self._surface, c, (self._x + self._width//2, self._y + self._height//2), self._height//2)
        pass

    def _drawBar(self, c):
        pygame.draw.rect(self._surface, c, self._rect, width=1)
        pass

    def draw(self):

        c = self._inActiveColor
        if self._active:
            c = self._activeColor

        self._drawBar(c)
        self._drawHandle(c)
        
        
        pass