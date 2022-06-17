from pygame_widgets_plus.widget import WidgetBase
from pygame_widgets_plus.widgets.option import Option
from pygame_widgets_plus.mouse import MouseHandler, MouseState
from pygame_widgets_plus.helpers import input2Color

import pygame.draw

class MultipleChoice(WidgetBase):
    def __init__(self, surface, x, y, width, height, **kwargs):
        super().__init__(surface, x, y, width, height,
                         kwargs.get("onMouseClicked", None), kwargs.get("onMouseClickedArgs", self),
                         kwargs.get("onMousePressed", None), kwargs.get("onMousePressedArgs", self),
                         kwargs.get("onMouseReleased", None), kwargs.get("onMouseReleasedArgs", self),
                         kwargs.get("onMouseMoved", None), kwargs.get("onMouseMovedArgs", self))
        self._style = kwargs.get("style", "circle")
        self._offset = y

    def option(self, text="option"):
        self._children.append(Option(self._surface, self._x, self._offset, style=self._style))
        self._offset += 5

    def update(self):
        for o in self._children:
            if (o.doesCollide(MouseHandler.mouseX, MouseHandler.mouseY) and (MouseHandler.state == MouseState.MOUSECLICK)):
                o.active = not o.active

    def draw(self):
        for o in self._children:
            o.draw()