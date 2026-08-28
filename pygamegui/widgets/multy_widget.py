from .group import Group
import pygame

class Multy_widget(Group):
    def __init__(self, parent = None, margin=(0, 0)):
        super().__init__(parent, 1, 1, False, margin)
    def render(self, window, x=0, y=0, size=(-1, -1), debug_outlines = False):
        for child in self.children:
            child.render(window, x, y, size, (debug_outlines+1 if debug_outlines else False))