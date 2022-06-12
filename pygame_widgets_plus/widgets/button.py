from pygame_widgets_plus.widget import WidgetBase
from pygame_widgets_plus.mouse import MouseHandler, MouseState
from pygame_widgets_plus.helpers import input2Color

import pygame.draw

class Button(WidgetBase):
    def __init__(self, surface, x, y, width, height, **kwargs):
        super().__init__(surface, x, y, width, height,
                         kwargs.get("onMouseClicked", None), kwargs.get("onMouseClickedArgs", self),
                         kwargs.get("onMousePressed", None), kwargs.get("onMousePressedArgs", self),
                         kwargs.get("onMouseReleased", None), kwargs.get("onMouseReleasedArgs", self),
                         kwargs.get("onMouseMoved", None), kwargs.get("onMouseMovedArgs", self))

        self._isPressed = False
        self._isHovered = False
        self._hasRun = False

        self._font = pygame.font.Font('freesansbold.ttf', 32)
        self._text = kwargs.get("text", "")
        self._renderedText = self._font.render(self._text, False, input2Color("black"))
        self._renderedTextRect = self._renderedText.get_rect()
        self._renderedTextRect.center = (x + width//2, y + height//2)

        self._defaultColor = input2Color(kwargs.get("defaultColor", "green"))
        self._hoverColor = input2Color(kwargs.get("hoverColor", "red"))
        self._pressColor = input2Color(kwargs.get("pressColor", "blue"))

        self._borderWidth = kwargs.get("borderWidth", 0)
        self._borderRadius = kwargs.get("borderRadius", 10)
        self._borderColor = input2Color(kwargs.get("borderColor", "yellow"))

    def doesCollide(self, x, y):
        return self._rect.collidepoint(x, y)

    def update(self):
        if self.doesCollide(MouseHandler.mouseX, MouseHandler.mouseY):
            self._isHovered = True
            if (MouseHandler.state == MouseState.MOUSEBUTTONDOWN):
                self._isPressed = True
            else:
                self._isPressed = False
        else:
            self._isHovered = False
            self._isPressed = False

        

        # @TODO: move this functionality to WidgetBase
        if self._isPressed and self._onMousePressed and not self._hasRun:
            self._onMousePressed(self._onMousePressedArgs)
            self._hasRun = True

        if not self._isPressed:
            self._hasRun = False
    
    def draw(self):
        c = self._defaultColor

        if self._isPressed:
            c = self._pressColor
        elif self._isHovered:
            c = self._hoverColor

        pygame.draw.rect(self._surface, c, self._rect, border_radius=self._borderRadius)
        if self._borderWidth:
            pygame.draw.rect(self._surface, self._borderColor, self._rect, border_radius=self._borderRadius, width=self._borderWidth)

        self._surface.blit(self._renderedText, self._renderedTextRect)