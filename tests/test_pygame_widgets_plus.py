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

    b = Button(screen, 20, 20, 100, 100, text="Button", defaultColor="purple", hoverColor="orange", pressColor="black", borderWidth=3, onMousePressed=output)

    # main game loop
    done = 0
    while not done:
        screen.fill("white")

        EventManager.update(pygame.event.get())

        
        b.update()
        b.draw()

        pygame.display.flip()
        
        clock.tick(50)
    pygame.quit()

    
    
