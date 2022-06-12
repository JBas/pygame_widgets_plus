import pygame.mouse

class MouseHandler:

    mouseX = None
    mouseY = None

    def update():
        (MouseHandler.mouseX, MouseHandler.mouseY) = pygame.mouse.get_pos()
        print(MouseHandler.mouseX)
        pass