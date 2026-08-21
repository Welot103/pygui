from __future__ import annotations
from .abstract_widget import Widget
import pygame

class Image(Widget):
    def __init__(self, parent = None, image_path=None, width=1, height=1, margin=(0, 0)):
        super().__init__(parent, width, height, margin)
        self.image_path = image_path
    def render(self, window, x=0, y=0, size=(-1, -1), debug_outlines = False):
        img = pygame.image.load(self.image_path)
        window.blit(img, (x, y))
