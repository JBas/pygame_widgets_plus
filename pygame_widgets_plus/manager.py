from pygame_widgets_plus.mouse import MouseHandler, MouseState
from pygame_widgets_plus.keyboard import KeyboardHandler

class WidgetManager:
    _widgets = []

    def addWidget(w):
        WidgetManager._widgets.append(w)

    def update():
        for w in WidgetManager._widgets:
            w.update()

    def draw():
        for w in WidgetManager._widgets:
            w.draw()

class EventManager:

    def update(event):
        MouseHandler.update(event)
        KeyboardHandler.update(event)

        if MouseHandler.state == MouseState.MOUSECLICK:
            EventManager.mouseClicked(event)
        elif MouseHandler.state == MouseState.MOUSEBUTTONDOWN:
            EventManager.mousePressed(event)
        elif MouseHandler.state == MouseState.MOUSEDRAGGED:
            EventManager.mouseDragged(event)
        
    def keyPressed(event):
        pass

    def mouseClicked(event):
        pass
        
    def mousePressed(event):
        pass

    def mouseDragged(event):
        pass