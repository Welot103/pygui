from __future__ import annotations
from .abstract_widget import Widget
import pygame

class Image(Widget):
    def __init__(self, parent: Widget = None, image_path=None, save_proportions=False, width=1, height=1, margin=(0, 0)):
        super().__init__(parent, width, height, margin)
        self.image_path = image_path
        self.save_proportions = save_proportions
    def render(self, window, x=0, y=0, size=(-1, -1), debug_outlines = False):
        from PIL import Image
        with Image.open(self.image_path) as img:
            if self.save_proportions:
                img.thumbnail(size)
            else:
                size = list(size)
                size[0] = int(size[0])
                size[1] = int(size[1])
                img = img.resize(size)
            raw_data = img.tobytes()
            surface = pygame.image.fromstring(raw_data, img.size, img.mode)
            window.blit(surface.convert_alpha(), (x, y))
