from ..styles.button_style import ButtonStyle
from .size_box import Size_box
import pygame

class Button(Size_box):
    def __init__(self, parent=None, width=1, height=1, vertical=False, margin=(0, 0), 
                max_size_px=(200, 100), side="top+left", on_click=None, style: ButtonStyle = None):
        super().__init__(parent, width, height, vertical, margin, max_size_px, side)
        self.on_click = on_click
        self.box = [0, 0, 0, 0]
        self.click = False
        
        if style is None:
            style = ButtonStyle()
            style.set_default()
        style.apply(self)

    def on_mouse(self):
        pos = pygame.mouse.get_pos()
        if self.box[0] <= pos[0] <= self.box[0]+self.box[2]:
            if self.box[1] <= pos[1] <= self.box[1]+self.box[3]:
                return True
        return False

    def render(self, window, x=0, y=0, size=(-1, -1), debug_outlines=False):
        self.box = [x, y, *size]
        if self.click:
            color = self.bg_click_color
        elif self.on_mouse():
            color = self.bg_color_hover
        else:
            color = self.bg_color
        pygame.draw.rect(window, color, (x, y, *size), border_radius=self.border_radius)
        pygame.draw.rect(window, self.border_color, (x, y, *size), width=self.border_size, 
                        border_radius=self.border_radius)

        return super().render(window, x+self.border_size/2, y+self.border_size/2, 
                                (size[0]-self.border_size, size[1]-self.border_size), debug_outlines)
    
    def check_events(self, events: list[pygame.event.Event]):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.on_mouse():
                    self.click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if self.on_mouse() and self.click:
                    self.on_click()
                self.click = False
        return super().check_events(events)