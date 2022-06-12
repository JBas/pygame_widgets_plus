from pygame_widgets_plus.mouse import MouseHandler

class EventManager:

    def update(events):
        for event in events:
            MouseHandler.update(event)
            # KeyboardHandler.update(event)
        
    def keyPressed(self):
        pass

    def mouseClicked(self):
        pass

    def mouseDragged(self):
        pass