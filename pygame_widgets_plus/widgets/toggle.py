from pygame_widgets_plus.widget import WidgetBase
from pygame_widgets_plus.widgets import Slider
from pygame_widgets_plus.mouse import MouseHandler, MouseState
from pygame_widgets_plus.helpers import input2Color

import pygame.draw

class Toggle(Slider):
    def __init__(self, surface, x, y, width, height, **kwargs):
        super().__init__(surface, x, y, width, height)
        self._isClicked = False
        self._isPressed = False

    def _doesCollide(self, x, y):
        return WidgetBase._doesCollide(self, MouseHandler.mouseX, MouseHandler.mouseY)

    def update(self):        
        if self._doesCollide(MouseHandler.mouseX, MouseHandler.mouseY):
            if (MouseHandler.state == MouseState.MOUSEBUTTONDOWN):
                self._active = not self._active

        if self._active:
            if self._onMouseClicked:
                self._onMouseClicked(self._onMouseClickedArgs)

            self._handleRect.centerx = self._barRect.right
        else:
            self._handleRect.centerx = self._barRect.left
        
        self._barRectProgress.width = self._handleRect.centerx - self._barRectProgress.left
        self._barRectProgress.right = self._handleRect.centerx


# class Toggle(WidgetBase):
#     def __init__(self, surface, x, y, width, height, **kwargs):
#         super().__init__(surface, x, y, width, height, True,
#                          kwargs.get("onMouseClicked", None), kwargs.get("onMouseClickedArgs", self),
#                          kwargs.get("onMousePressed", None), kwargs.get("onMousePressedArgs", self),
#                          kwargs.get("onMouseReleased", None), kwargs.get("onMouseReleasedArgs", self),
#                          kwargs.get("onMouseMoved", None), kwargs.get("onMouseMovedArgs", self))

#         self._active = False
#         self._rect.center = (x, y)

#         self._activeColor = input2Color(kwargs.get("activeColor", "blue"))
#         self._inActiveColor = input2Color(kwargs.get("activeColor", "grey"))

#     @property
#     def active(self):
#         return self._active

#     def update(self):
#         if self._doesCollide(MouseHandler.mouseX, MouseHandler.mouseY):
#             if (MouseHandler.state == MouseState.MOUSECLICK):
#                 self._active = not self._active
#         pass

#     def _drawHandle(self, c):
#         if self.active:
#             pygame.draw.circle(self._surface, c, (self._x + self._width//2, self._y), self._height//2)
#         else:
#             pygame.draw.circle(self._surface, c, (self._x - self._width//2, self._y), self._height//2)
#         pass

#     def _drawBar(self, c):
#         pygame.draw.rect(self._surface, c, self._rect, width=1)
#         pass

#     def draw(self):

#         c = self._inActiveColor
#         if self.active:
#             c = self._activeColor

#         self._drawBar(c)
#         self._drawHandle(c)
        
        
#         pass