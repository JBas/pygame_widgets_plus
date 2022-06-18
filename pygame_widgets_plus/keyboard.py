import pygame

class meta_KeyboardHandler(type):
    def __init__(cls, *args, **kwargs):
        cls._buffer = ""

    @property
    def buffer(cls):
        return cls._buffer

    @buffer.setter
    def buffer(cls, s):
        cls._buffer = s

class KeyboardHandler(metaclass=meta_KeyboardHandler):

    # not thread-safe
    def consume():
        if (len(KeyboardHandler.buffer) <= 0):
            return ""
            
        c = KeyboardHandler.buffer[0]
        KeyboardHandler.buffer = KeyboardHandler.buffer[1:]
        return c

    # not thread-safe
    def flush():
        KeyboardHandler.buffer = ""
        
    def update(event):
        if (event.type == pygame.KEYDOWN):
            
            KeyboardHandler.buffer += event.unicode
        pass