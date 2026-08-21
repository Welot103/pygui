from __future__ import annotations
from .abstract_widget import Widget
from ..styles.label_style import LabelStyle
import pygame

class Label(Widget):
    def __init__(self, parent = None, width=1, height=1, text="Pygame Gui", style: LabelStyle = None):
        super().__init__(parent, width, height, (0, 0))
        self.text = text

        if style is None:
            style = LabelStyle()
            style.set_default()
        style.apply(self)
    
    def __render_line(self, window: pygame.Surface, x, y, size, text, text_size, h):
        if self.text_side == "left":
            window.blit(self.font.render(text, False, self.color), (x, y+h+text_size[1]))
        elif self.text_side == "right":
            window.blit(self.font.render(text, False, self.color), (x+size[0]-text_size[0], y+h+text_size[1]))
        elif self.text_side == "center":
            window.blit(self.font.render(text, False, self.color), (x+size[0]//2-text_size[0]//2, y+h+text_size[1]))
    
    def render(self, window: pygame.Surface, x, y, size, debug_outlines = False):
        start_i = 0
        i = 0
        h = 0
        while True:
            i += 1
            text_size = self.font.size(self.text[start_i:i])
            if text_size[0] > size[0]:
                self.__render_line(window, x, y, size, self.text[start_i:i-1], text_size, h)
                start_i = i-1
                h += text_size[1]
            if h >= size[1]:
                break
            if i >= len(self.text)-1:
                self.__render_line(window, x, y, size, self.text[start_i:i+1], text_size, h)
                break
        