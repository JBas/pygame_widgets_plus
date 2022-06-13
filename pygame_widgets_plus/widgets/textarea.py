from pygame_widgets_plus.widget import WidgetBase

import pygame

class TextArea(WidgetBase):

    def __init__(self, surface, x, y, width, height, **kwargs):
        super().__init__(surface, x, y, width, height)

        self._text = kwargs.get("text", "What would you like to say?")
        self._textArea = pygame.Surface((width, height))
        self._textArea.fill("white")

        font = pygame.font.Font(None, 12)
        self.xtext = font.render(self._text, False, "green")
        self.xtextpos = self.xtext.get_rect()
        self._textArea.blit(self.xtext, self.xtextpos)

        self._textArea.scroll(20, 20)

        self._active = False

    def update(self):
        pass

    def draw(self):
            
        pygame.draw.rect(self._surface, (51, 51, 51), self._rect, border_radius=10)
        # self._surface.blit(self._textArea, self._rect)
        pass