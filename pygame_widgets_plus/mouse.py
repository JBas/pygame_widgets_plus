import pygame.mouse

from enum import Enum, auto

class MouseState(Enum):
    MOUSEIDLE = auto()
    MOUSEMOTION = auto()
    MOUSEBUTTONUP = auto()
    MOUSEBUTTONDOWN = auto()
    MOUSEDRAGGED = auto()

class MouseHandler:
    
    _mouseX = None
    _mouseY = None

    _state = MouseState.MOUSEIDLE

    _isUp = True

    @property
    def mouseX():
        return MouseHandler._mouseX

    @property
    def mouseY():
        return MouseHandler._mouseY

    @property
    def state():
        return MouseHandler._state

    def update(event):
        (MouseHandler.mouseX, MouseHandler.mouseY) = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP:
            MouseHandler.state = MouseState.MOUSEBUTTONUP
            MouseHandler._isUp = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            MouseHandler.state = MouseState.MOUSEBUTTONDOWN
            MouseHandler._isUp = False
        elif event.type == pygame.MOUSEMOTION:
            if (not MouseHandler._isUp):
                MouseHandler.state = MouseState.MOUSEDRAGGED
            else:
                MouseHandler.state = MouseState.MOUSEMOTION
        else:
            MouseHandler.state = MouseState.MOUSEIDLE   