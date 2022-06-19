from pygame_widgets_plus.widget import WidgetBase
from pygame_widgets_plus.mouse import MouseHandler, MouseState
from pygame_widgets_plus.helpers import input2Color

import pygame.draw

class Button(WidgetBase):
    def __init__(self, surface, x, y, width, height, **kwargs):
        super().__init__(surface, x, y, width, height, True,
                         kwargs.get("onMouseClicked", None), kwargs.get("onMouseClickedArgs", self),
                         kwargs.get("onMousePressed", None), kwargs.get("onMousePressedArgs", self),
                         kwargs.get("onMouseReleased", None), kwargs.get("onMouseReleasedArgs", self),
                         kwargs.get("onMouseMoved", None), kwargs.get("onMouseMovedArgs", self))

        self._isClicked = False
        self._isPressed = False
        self._isHovered = False

        self._font = pygame.font.Font('freesansbold.ttf', 12)
        self._text = kwargs.get("text", "Button")
        self._renderedText = self._font.render(self._text, False, input2Color("black"))
        self._renderedTextRect = self._renderedText.get_rect()
        self._renderedTextRect.center = self._rect.center

        self._defaultColor = input2Color(kwargs.get("defaultColor", "azure1"))
        self._hoverColor = input2Color(kwargs.get("hoverColor", "azure2"))
        self._pressColor = input2Color(kwargs.get("pressColor", "red"))

        self._borderWidth = kwargs.get("borderWidth", 1)
        self._borderRadius = kwargs.get("borderRadius", 10)
        self._borderColor = input2Color(kwargs.get("borderColor", "cadetblue3"))

    def update(self):
        
        if self._doesCollide(MouseHandler.mouseX, MouseHandler.mouseY):
            self._isHovered = True
            if (MouseHandler.state == MouseState.MOUSECLICK):
                self._isClicked = True
                self._isPressed = True
            elif (MouseHandler.state == MouseState.MOUSEBUTTONDOWN):
                self._isPressed = True
            else:
                self._isClicked = False
                self._isPressed = False
        else:
            self._isHovered = False
            self._isClicked = False
            self._isPressed = False

        # print(self._isHovered, self._isPressed)

        if self._isClicked and self._onMouseClicked:
            self._onMouseClicked(self._onMouseClickedArgs)
    
    def draw(self):
        if self._show:
            c = self._defaultColor
    
            if self._isPressed:
                c = self._pressColor
            elif self._isHovered:
                c = self._hoverColor
    
            pygame.draw.rect(self._surface, c, self._rect, border_radius=self._borderRadius)
            if self._borderWidth:
                pygame.draw.rect(self._surface, self._borderColor, self._rect, border_radius=self._borderRadius, width=self._borderWidth)
    
            self._surface.blit(self._renderedText, self._renderedTextRect)