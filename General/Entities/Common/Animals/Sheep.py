from Animal import Animal
from ImageLoader import ImageLoader

class Sheep(Animal):
    """description of class"""

    def __init__(self, a = 0, w = None):
        if w == None:
            Animal.__init__(self, 4, 4, 0, None, 'S')
        else:
            Animal.__init__(self, 4, 4, a, w, 'S')

    @property
    def image(self):
        return ImageLoader.sheep

    @property
    def string(self):
        return "Sheep"
