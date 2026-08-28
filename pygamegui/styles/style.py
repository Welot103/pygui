from .. import config

class Style:
    '''
        The base class for all other style classes.
        Its doing setattr for self.apply(object) with all kwargs
    '''
    def __init__(self, **kwargs):
        self.keys = list(kwargs.keys())
        for k, v in kwargs.items():
            setattr(self, k, v)
    def set_default(self):
        self.color = config.default_style["color"]
        for k in self.keys:
            setattr(self, k, config.default_style[k])
    def apply(self, object):
        for k in self.keys:
            setattr(object, k, getattr(self, k))