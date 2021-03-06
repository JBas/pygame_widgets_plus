from abc import ABC, abstractmethod

from pygame_widgets_plus.manager import WidgetManager

import pygame

class WidgetBase(ABC):
    def __init__(self, surface, x, y, width, height, isTopLevelParent=True,
                 onMouseClicked=None, onMouseClickedArgs=None,
                 onMousePressed=None, onMousePressedArgs=None,
                 onMouseReleased=None, onMouseReleasedArgs=None,
                 onMouseMoved=None, onMouseMovedArgs=None):
        super().__init__()
        self._surface = surface
        self._rect = pygame.Rect(x, y, width, height)
        self._rect.center = (x, y)
        self._value = None

        self._onMouseClicked = onMouseClicked
        self._onMouseClickedArgs = onMouseClickedArgs
        
        self._onMousePressed = onMousePressed
        self._onMousePressedArgs = onMousePressedArgs
        
        self._onMouseReleased = onMouseReleased
        self._onMouseReleasedArgs = onMouseReleasedArgs
        
        self._onMouseMoved = onMouseMoved
        self._onMouseMovedArgs = onMouseMovedArgs
        
        self._show = True

        self._isTopLevelParent = isTopLevelParent
        
        if (isTopLevelParent):
            self._children = []
            WidgetManager.addWidget(self)
        else:
            self._children = None
        pass

    def _doesCollide(self, x, y):
        return self._rect.collidepoint(x, y)

    def show(self):
        self._show = True

    def hide(self):
        self._show = False

    def value(self):
        return self._value

    def value(self, value):
        self._value = value

    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def draw(self):
        pass