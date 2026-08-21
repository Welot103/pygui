from .group import Group
import pygame

class Size_box(Group):
    def __init__(self, parent = None, width=1, height=1, vertical=False, margin=(0, 0), max_size_px=(200, 100), side="top+left"):
        super().__init__(parent, width, height, vertical, margin)
        self.max_size_px = max_size_px
        self.side = side
    def render(self, window: pygame.Surface, x=0, y=0, size=(-1, -1), debug_outlines = False):
        size = list(size)
        if size[0] == -1:
            size[0] = window.get_size()[0]
        if size[1] == -1:
            size[1] = window.get_size()[1]

        self_size = (min(size[0], self.max_size_px[0]), min(size[1], self.max_size_px[1]))
        if "right" in self.side:
            x += size[0] - self_size[0]
        if "bottom" in self.side:
            y += size[1] - self_size[1]

        super().render(window, x, y, self_size, debug_outlines)