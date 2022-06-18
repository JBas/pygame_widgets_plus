from pygame_widgets_plus.widget import WidgetBase
from pygame_widgets_plus.widgets.option import Option
from pygame_widgets_plus.mouse import MouseHandler, MouseState
from pygame_widgets_plus.helpers import input2Color

import pygame.draw

class MultipleChoice(WidgetBase):
    def __init__(self, surface, x, y, width, height, **kwargs):
        super().__init__(surface, x, y, width, height, True,
                         kwargs.get("onMouseClicked", None), kwargs.get("onMouseClickedArgs", self),
                         kwargs.get("onMousePressed", None), kwargs.get("onMousePressedArgs", self),
                         kwargs.get("onMouseReleased", None), kwargs.get("onMouseReleasedArgs", self),
                         kwargs.get("onMouseMoved", None), kwargs.get("onMouseMovedArgs", self))
        self._style = kwargs.get("style", "circle")
        self._offsetX = 10
        self._offsetY = 0

    def option(self, text="option"):
        self._children.append(Option(self._surface, self._rect.left + self._offsetX, self._rect.top + self._offsetY, style=self._style))
        self._offsetY += 20

    def update(self):
        for o in self._children:
            if (o.doesCollide(MouseHandler.mouseX, MouseHandler.mouseY) and (MouseHandler.state == MouseState.MOUSECLICK)):
                o.active = not o.active

    def draw(self):
        pygame.draw.rect(self._surface, (200, 200, 200), self._rect)
        for o in self._children:
            o.draw()