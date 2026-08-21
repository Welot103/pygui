from __future__ import annotations
import pygame

class Widget:
    def __init__(self, parent: Widget = None, width=1, height=1, margin=(0, 0)):
        if parent is not None:
            parent.add_child(self)
        self.width, self.height = width, height
        self.margin = margin
    def render(self, window: pygame.Surface, x=0, y=0, size=(-1, -1), debug_outlines: int = False): ...
    def check_events(self, events: list[pygame.event.Event]) -> bool: ...