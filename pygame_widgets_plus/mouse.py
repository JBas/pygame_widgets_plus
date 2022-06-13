import pygame.mouse

from enum import Enum, auto

class MouseState(Enum):
    MOUSEIDLE = auto()
    MOUSEMOTION = auto()
    MOUSECLICK = auto()
    MOUSEBUTTONUP = auto()
    MOUSEBUTTONDOWN = auto()
    MOUSEDRAGGED = auto()

class meta_MouseHandler(type):
    def __init__(cls, *args, **kwargs):
        cls._mouseX = -1
        cls._mouseY = -1
    
        cls._prevState = MouseState.MOUSEIDLE
        cls._state = MouseState.MOUSEIDLE
        
    @property
    def mouseX(cls):
        return cls._mouseX

    @mouseX.setter
    def mouseX(cls, x):
        cls._mouseX = x

    @property
    def mouseY(cls):
        return cls._mouseY

    @mouseY.setter
    def mouseY(cls, y):
        cls._mouseY = y

    @property
    def state(cls):
        return cls._state

    @state.setter
    def state(cls, s):
        cls._state = s

    @property
    def prevState(cls):
        return cls._prevState

    @prevState.setter
    def prevState(cls, p):
        cls._prevState = p if (p != MouseState.MOUSEIDLE) else cls._prevState


class MouseHandler(metaclass=meta_MouseHandler):

    def update(event):

        if event.type == pygame.MOUSEBUTTONUP:
            (MouseHandler.mouseX, MouseHandler.mouseY) = event.pos
            if MouseHandler.prevState == MouseState.MOUSEBUTTONDOWN:
                MouseHandler.prevState = MouseHandler.state
                MouseHandler.state = MouseState.MOUSECLICK
            else:
                MouseHandler.prevState = MouseHandler.state
                MouseHandler.state = MouseState.MOUSEBUTTONUP
                
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (MouseHandler.mouseX, MouseHandler.mouseY) = event.pos
            MouseHandler.prevState = MouseHandler.state
            MouseHandler.state = MouseState.MOUSEBUTTONDOWN
            
        elif event.type == pygame.MOUSEMOTION:
            (MouseHandler.mouseX, MouseHandler.mouseY) = event.pos
            if (MouseHandler.prevState == MouseState.MOUSEBUTTONDOWN):
                MouseHandler.prevState = MouseHandler.state
                MouseHandler.state = MouseState.MOUSEDRAGGED
            else:
                MouseHandler.prevState = MouseHandler.state
                MouseHandler.state = MouseState.MOUSEMOTION
                
        else:
            MouseHandler.prevState = MouseHandler.state
            MouseHandler.state = MouseState.MOUSEIDLE