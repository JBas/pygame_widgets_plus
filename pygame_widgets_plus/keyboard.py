import pygame

class KeyboardHandler:
    
    def update(event):
            
        if (event.type == pygame.KEYDOWN):
            print(event.unicode)
        pass