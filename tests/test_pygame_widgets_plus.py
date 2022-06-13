from pygame_widgets_plus import *

def output(self):
    print("WooHoo!")

def test_version():
    assert __version__ == '0.1.0'

def test_button():
    b = Button()
    assert type(b) == Button

if __name__=="__main__":
    import pygame
    
    pygame.init()

    screen = pygame.display.set_mode((600, 400))
    clock = pygame.time.Clock()

    b = Slider(screen, 300, 200, 200, 50)

    # main game loop
    done = 0
    while not done:
        screen.fill("white")

        for e in pygame.event.get():
            EventManager.update(e)
            WidgetManager.update()
        WidgetManager.draw()

        pygame.display.flip()
        
        clock.tick(60)
    pygame.quit()

    
    
