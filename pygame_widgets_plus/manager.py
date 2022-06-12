from pygame_widgets_plus.mouse import MouseHandler, MouseState
from pygame_widgets_plus.keyboard import KeyboardHandler

class EventManager:

    def update(events):
        for event in events:
            MouseHandler.update(event)
            KeyboardHandler.update(event)

            if MouseHandler.state == MouseState.MOUSEBUTTONDOWN:
                EventManager.mousePressed(event)
            elif MouseHandler.state == MouseState.MOUSEDRAGGED:
                EventManager.mouseDragged(event)
        
    def keyPressed(event):
        pass

    def mousePressed(event):
        pass

    def mouseDragged(event):
        pass