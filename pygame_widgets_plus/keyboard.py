import pygame
from threading import Lock

class meta_KeyboardHandler(type):
    def __init__(cls, *args, **kwargs):
        cls._buffer = ""
        cls._lock = Lock()
    
    @property
    def buffer(cls):
        return cls._buffer

    @buffer.setter
    def buffer(cls, s):
        cls._buffer = s

class KeyboardHandler(metaclass=meta_KeyboardHandler):

    def consume():
        
        KeyboardHandler._lock.acquire()
        
        if (len(KeyboardHandler.buffer) <= 0):
            KeyboardHandler._lock.release()
            return ""
            
        c = KeyboardHandler.buffer[0]
        KeyboardHandler.buffer = KeyboardHandler.buffer[1:]
        
        KeyboardHandler._lock.release()
        
        return c

    def flush():
        KeyboardHandler._lock.acquire()
        KeyboardHandler.buffer = ""
        KeyboardHandler._lock.release()
        
    def update(event):
        if (event.type == pygame.KEYDOWN):
            KeyboardHandler._lock.acquire()
            KeyboardHandler.buffer += event.unicode
            KeyboardHandler._lock.release()
        pass