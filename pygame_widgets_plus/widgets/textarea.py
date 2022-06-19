from pygame_widgets_plus.widget import WidgetBase
from pygame_widgets_plus.keyboard import KeyboardHandler
from pygame_widgets_plus.mouse import MouseHandler, MouseState

from pygame_widgets_plus.helpers import PRINT

import pygame

class TextArea(WidgetBase):

    def __init__(self, surface, x, y, width, height, **kwargs):
        super().__init__(surface, x, y, width, height)

        self._textList = [kwargs.get("text", "")]
        self._textArea = pygame.Surface((width, height))
        self._textArea.fill("white")
        
        self._offsets = [0]

        self._font = pygame.font.Font(None, 36)

        # self._textArea.scroll(20, 20)

        self._active = False

        self._line = 0
        self._cursorLine = 0
        self._cursorPos = 0

    @property
    def text(self):
        return "".join(self._textList)

    def update(self):

        if self._doesCollide(MouseHandler.mouseX, MouseHandler.mouseY):
            if (MouseHandler.state == MouseState.MOUSEBUTTONDOWN):
                self._active = True
                KeyboardHandler.flush()
        elif (MouseHandler.state == MouseState.MOUSEBUTTONDOWN):
            self._active = False
            KeyboardHandler.flush()

        if (self._active):
            c = KeyboardHandler.consume()
            if c == "":
                return
  
            if (ord(c) == 0x8 and self._line >= 0):
                if len(self._textList[self._line]) > 0:
                    PRINT(f"CURSOR old: {self._cursorPos}", end=", ")

                    self._cursorPos -= 1
                    left = self._textList[self._line][:self._cursorPos]
                    right = self._textList[self._line][self._cursorPos+1:]
                    self._textList[self._line] = left + right
                    PRINT(f"CURSOR new: {self._cursorPos}")
                elif (self._line != 0):
                    PRINT(f"POP old: {self._line}", end=", ")
                    self._textList.pop()
                    self._offsets.pop()
                    self._line -= 1
                    self._cursorLine -= 1
                    PRINT(f"CURSOR old: {self._cursorPos}", end=", ")
                    self._cursorPos = len(self._textList[self._line])
                    PRINT(f"CURSOR new: {self._cursorPos}", end= ", ")
                    PRINT(f"POP new: {self._line}")
                    
            elif (c == "\n" or c == "\r"):
                PRINT(f"LINE old: {self._line}", end=", ")
                self._line += 1
                self._cursorLine += 1
                self._textList.append("")
                self._offsets.append(self._line*self._font.get_linesize())
                PRINT(f"CURSOR old: {self._cursorPos}", end=", ")
                self._cursorPos = 0
                PRINT(f"CURSOR new: {self._cursorPos}", end= ", ")
                PRINT(f"LINE new: {self._line}")
            else:
                left = self._textList[self._line][:self._cursorPos]
                right = self._textList[self._line][self._cursorPos:]
                
                self._textList[self._line] =  left + c + right
                PRINT(f"CURSOR old: {self._cursorPos}", end=", ")
                self._cursorPos += 1
                PRINT(f"CURSOR new: {self._cursorPos}")

        pass

    def _cursorBlink(self):
        
        return True

    def draw(self):
        if self._show:
            self._textArea.fill("white")
            
            for line in range(len(self._textList)):

                if line == self._cursorLine and self._active:
                    left = self._textList[line][:self._cursorPos]
                    right = self._textList[line][self._cursorPos:]

                    xtextL = self._font.render(left + "|", True, "black")
                    xtextposL = xtextL.get_rect()
                    xtextposL.top = self._offsets[line]

                    xtextR = self._font.render(right, True, "black")
                    xtextposR = xtextR.get_rect()
                    xtextposR.top = self._offsets[line]
                    xtextposR.left = xtextposL.right
                    
                    self._textArea.blit(xtextR, xtextposR)
                    self._textArea.blit(xtextL, xtextposL)
                else:
                
                    xtext = self._font.render(self._textList[line], True, "black")
                    xtextpos = xtext.get_rect()
                    xtextpos.top = self._offsets[line]
                    
                    self._textArea.blit(xtext, xtextpos)
                
            pygame.draw.rect(self._surface, (100, 100, 100), self._rect, border_radius=10)
            self._surface.blit(self._textArea, self._rect)
    
            if (self._active):
                pygame.draw.rect(self._surface, (100, 100, 255), self._rect, border_radius=10, width=2)
        pass