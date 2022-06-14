from pygame_widgets_plus.widget import WidgetBase
from pygame_widgets_plus.mouse import MouseHandler, MouseState
from pygame_widgets_plus.helpers import input2Color

import pygame.draw

class Slider(WidgetBase):
    def __init__(self, surface, x, y, width, height, **kwargs):
        super().__init__(surface, x, y, width, height,
                         kwargs.get("onMouseClicked", None), kwargs.get("onMouseClickedArgs", self),
                         kwargs.get("onMousePressed", None), kwargs.get("onMousePressedArgs", self),
                         kwargs.get("onMouseReleased", None), kwargs.get("onMouseReleasedArgs", self),
                         kwargs.get("onMouseMoved", None), kwargs.get("onMouseMovedArgs", self))

        self._min = kwargs.get("min", 0)
        self._max = kwargs.get("max", 10)
        self._value = kwargs.get("value", 5)
        self._step = kwargs.get("step", 1)
        
        self._rect.center = (x, y)

        self._barRect = pygame.Rect(x, y, width, height//6)
        self._barRect.center = (x, y)
        self._barRectProgress = self._barRect.copy()

        self._physDist = self._barRect.right - self._barRect.left

        self._handleRadius = height // 4
        self._handleRect = pygame.Rect(x, y, self._handleRadius*2, self._handleRadius*2)
        self._handleRect.center = self._calcPosFromValue()
        
        self._active = False
        

    def _doesCollide(self, x, y):
        return self._handleRect.collidepoint(x, y)

    # @TODO: needs to get fixed
    def _calcPosFromValue(self):
        d = self._max - self._min + 1
        f = self._value / d

        x = self._barRect.left + self._physDist*f

        return (x, self._barRect.centery)
        

    # @TODO: needs to get fixed
    def _calcValueFromPos(self):
        valDist = self._handleRect.centerx - self._barRect.left
        f = 1 - (self._physDist - valDist) / self._physDist
        
        return (self._max - self._min + 1)*f

    def update(self):
        if self._doesCollide(MouseHandler.mouseX, MouseHandler.mouseY):
            if (MouseHandler.state == MouseState.MOUSEBUTTONDOWN):
                self._active = True
        if (MouseHandler.state == MouseState.MOUSEBUTTONUP):
                self._active = False
            
        if self._active:       
            if MouseHandler.mouseX >= self._barRect.right:
                self._handleRect.centerx = self._barRect.right
            elif MouseHandler.mouseX <= self._barRect.left:
                self._handleRect.centerx = self._barRect.left
            else:
                self._handleRect.centerx = MouseHandler.mouseX
                
        self._barRectProgress.width = self._handleRect.centerx - self._barRectProgress.left
        self._barRectProgress.right = self._handleRect.centerx

        self._value = self._calcValueFromPos()
        print(self._value)

    def draw(self):
        c = (150, 150, 150)
        if self._active:
            c = (80, 80, 255)
        
        pygame.draw.rect(self._surface, (100, 100, 100), self._barRect, border_radius=20)
        pygame.draw.rect(self._surface, (100, 100, 255), self._barRectProgress, border_radius=20, border_top_right_radius=0, border_bottom_right_radius=0)
        pygame.draw.circle(self._surface, c, self._handleRect.center, self._handleRadius)
        pygame.draw.circle(self._surface, (255, 255, 255), self._handleRect.center, self._handleRadius, width=3)
        pygame.draw.circle(self._surface, (210, 210, 210), self._handleRect.center, self._handleRadius, width=1)
        pass