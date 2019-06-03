from Plant import Plant
from ImageLoader import ImageLoader

class Grass(Plant):
    """description of class"""
    
    def __init__(self, a = 0, w = None):
        if w == None:
            Plant.__init__(self, 0, 0, None, 0.07, 'G')
        else:
            Plant.__init__(self, 0, a, w, 0.07, 'G')

    @property
    def image(self):
        return ImageLoader.grass

    @property
    def string(self):
        return "Grass"