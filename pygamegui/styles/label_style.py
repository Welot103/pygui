import pygame
from .style import Style
from .. import config

class LabelStyle(Style):
    def __init__(self, color=(255, 255, 255), font_name=None, font_size=20, text_side="left"):
        super().__init__(color=color, font_name=font_name, font_size=font_size, text_side=text_side)
    def apply(self, object: 'Label'): # type: ignore
        from ..widgets.label import Label
        if isinstance(object, Label):
            object.color = self.color
            object.text_side = self.text_side
            object.font = pygame.font.Font(self.font_name, self.font_size)