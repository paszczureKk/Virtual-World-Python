from Plant import Plant
from ImageLoader import ImageLoader

class Dandelion(Plant):
    """description of class"""
    
    def __init__(self, a = 0, w = None):
        if w == None:
            Plant.__init__(self, 0, 0, None, 0.05, 'D')
        else:
            Plant.__init__(self, 0, a, w, 0.05, 'D')

    @property
    def image(self):
        return ImageLoader.dandelion

    def Action(self):
        for i in range(0, 3):
            Plant.Action(self)

    @property
    def string(self):
        return "Dandelion"