from pygame_widgets_plus import *

def output(self):
    print("WooHoo!")

def main():
    import pygame
    
    pygame.init()

    screen = pygame.display.set_mode((600, 400))
    clock = pygame.time.Clock()

    button = Button(screen, 50, 25, 100, 50)
    slider = Slider(screen, 50, 75, 100, 50)
    toggle = Toggle(screen, 50, 125, 50, 50)

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

    
main()
