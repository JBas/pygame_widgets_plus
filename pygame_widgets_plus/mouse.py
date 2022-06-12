import pygame.mouse

from enum import Enum, auto

class MouseState(Enum):
    MOUSEIDLE = auto()
    MOUSEMOTION = auto()
    MOUSECLICK = auto()
    MOUSEBUTTONUP = auto()
    MOUSEBUTTONDOWN = auto()
    MOUSEDRAGGED = auto()

class MouseHandler:
    
    _mouseX = None
    _mouseY = None

    _prevState = MouseState.MOUSEIDLE
    _state = MouseState.MOUSEIDLE

    _isUp = True

    @property
    def mouseX():
        return MouseHandler._mouseX

    @mouseX.setter
    def mouseX(x):
        MouseHandler._mouseX = x

    @property
    def mouseY():
        return MouseHandler._mouseY

    @mouseY.setter
    def mouseY(y):
        MouseHandler._mouseY = y

    @property
    def state():
        return MouseHandler._state

    @state.setter
    def state(s):
        MouseHandler._state = s

    @property
    def prevState():
        return MouseHandler._prevState

    @prevState.setter
    def prevState(p):
        MouseHandler._prevState = p if (p != MouseState.MOUSEIDLE) else MouseHandler.prevState

    def update(event):
        (MouseHandler.mouseX, MouseHandler.mouseY) = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP:
            if MouseHandler.prevState == MouseState.MOUSEBUTTONDOWN:
                MouseHandler.prevState = MouseHandler.state
                MouseHandler.state = MouseState.MOUSECLICK
            else:
                MouseHandler.prevState = MouseHandler.state
                MouseHandler.state = MouseState.MOUSEBUTTONUP
                
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            MouseHandler.prevState = MouseHandler.state
            MouseHandler.state = MouseState.MOUSEBUTTONDOWN
            
        elif event.type == pygame.MOUSEMOTION:

            if (MouseHandler._prevState == MouseState.MOUSEBUTTONDOWN):
                MouseHandler.prevState = MouseHandler.state
                MouseHandler.state = MouseState.MOUSEDRAGGED
            else:
                MouseHandler.prevState = MouseHandler.state
                MouseHandler.state = MouseState.MOUSEMOTION
                
        else:
            MouseHandler.prevState = MouseHandler.state
            MouseHandler.state = MouseState.MOUSEIDLE