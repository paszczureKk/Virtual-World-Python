from Animal import Animal
from ImageLoader import ImageLoader

class Wolf(Animal):
    """description of class"""
    
    def __init__(self, a = 0, w = None):
        if w == None:
            Animal.__init__(self, 9, 5, 0, None, 'W')
        else:
            super.__init__(self, 9, 5, a, w, 'W')

    @property
    def image(self):
        return ImageLoader.wolf

    @property
    def string(self):
        return "Wolf"