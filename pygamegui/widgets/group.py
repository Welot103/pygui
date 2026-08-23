from .abstract_widget import Widget
import pygame

class Group(Widget):
    """ 
        Widget for base allotment of widgets. Allow only in context with.
        
        with Group(...) as g0:
            Widget(g0, ...)
    """
    
    def __init__(self, parent: Widget = None, width=1, height=1, vertical = False, margin=(0, 0)):
        super().__init__(parent, width, height, margin)
        self.vertical = vertical
        self.is_open = False
        self.children = []
        self.last_boxes = []
    def __enter__(self):
        self.is_open = True
        return self
    def __exit__(self, exc_type, exc, tb):
        self.is_open = False
        return False
    def add_child(self, child: Widget):
        if self.is_open:
            self.children.append(child)
    def render(self, window: pygame.Surface, x=0, y=0, size=(-1, -1), debug_outlines: int = False):
        size = list(size)
        if size[0] == -1:
            size[0] = window.get_size()[0]
        if size[1] == -1:
            size[1] = window.get_size()[1]

        sum_kw = 0
        sum_kh = 0
        max_w = 0
        max_h = 0
        for child in self.children:
            sum_kw += child.width
            sum_kh += child.height
            max_w = max(max_w, child.width)
            max_h = max(max_h, child.height)

        self.last_boxes = []
        current_k = 0
        for child in self.children:
            if hasattr(child, "margin"):
                margin_x, margin_y = child.margin
            
            if not self.vertical:
                child_x = current_k / sum_kw * size[0] + x + margin_x
                child_y = y + margin_y
                child_w = child.width / sum_kw * size[0] - 1 - margin_x*2
                child_h = child.height / max_h * size[1] - 1 - margin_y*2
            else:
                child_x = x + margin_x
                child_y = current_k / sum_kh * size[1] + margin_y
                child_w = child.width / max_w * size[0] - 1 - margin_x*2
                child_h = child.height / sum_kh * size[1] - 1 - margin_y*2

            if debug_outlines:
                #print((child_x, child_y, child_w, child_h), debug_outlines)
                pygame.draw.rect(window, (0, 0, 255), (child_x, child_y, child_w, child_h), debug_outlines)
                pygame.draw.circle(window, (255, 0, 0), (child_x+child_w//2, child_y+child_h//2), debug_outlines)
            child.render(window, child_x, child_y, (child_w, child_h), (debug_outlines+1 if debug_outlines else False))
            self.last_boxes.append(((child_x, child_y, child_w, child_h), child))

            if not self.vertical:
                current_k += child.width
            else:
                current_k += child.height
    def check_events(self, events: list[pygame.event.Event]):
        for child in self.children:
            child.check_events(events)