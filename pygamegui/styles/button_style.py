from .style import Style

class ButtonStyle(Style):
    def __init__(self, border_color=(0, 0, 255), border_radius=5, border_size=7, 
                bg_color=(0, 0, 0), bg_color_hover=(0, 0, 150), bg_click_color=(0, 0, 100)):
        super().__init__(border_color=border_color, border_radius=border_radius, 
                        border_size=border_size, bg_color=bg_color, 
                        bg_color_hover=bg_color_hover, bg_click_color=bg_click_color)
