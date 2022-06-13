import pygame

class meta_KeyboardHandler(type):
    def __init__(cls, *args, **kwargs):
        cls._input = ""

    @property
    def input(cls):
        return cls._input

    @input.setter
    def input(cls, s):
        cls._input = s

class KeyboardHandler(metaclass=meta_KeyboardHandler):
    
    def update(event):
        if (event.type == pygame.KEYDOWN):
            KeyboardHandler.input += event.unicode
        pass