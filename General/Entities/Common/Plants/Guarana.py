from Plant import Plant
from ImageLoader import ImageLoader

class Guarana(Plant):
    """description of class"""
    
    def __init__(self, a = 0, w = None):
        if w == None:
            Plant.__init__(self, 0, 0, None, 0.07, 'U')
        else:
            Plant.__init__(self, 0, a, w, 0.07, 'U')

    @property
    def image(self):
        return ImageLoader.guarana

    def Collision(self, o):
        o.buff(3)

        Plant.Collision(self, o)

        return False

    @property
    def string(self):
        return "Grass"