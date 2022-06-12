from pygame_widgets_plus import *
from pygame_widgets_plus.mouse import MouseHandler

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
    pygame.display.set_caption("pygame Stars Example")
    white = 255, 240, 200
    black = 20, 20, 40
    screen.fill(black)

    # main game loop
    done = 0
    while not done:
        for e in pygame.event.get():
            if e.type == pygame.QUIT or (e.type == pygame.KEYUP and e.key == pygame.K_ESCAPE):
                done = 1
                break

        clock.tick(50)
    pygame.quit()

    
    
