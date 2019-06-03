from Plant import Plant
from ImageLoader import ImageLoader

class Belladonna(Plant):
    """description of class"""
    
    def __init__(self, a = 0, w = None):
        if w == None:
            Plant.__init__(self, 99, 0, None, 0.03, 'B')
        else:
            Plant.__init__(self, 99, a, w, 0.03, 'B')

    @property
    def image(self):
        return ImageLoader.belladonna

    def Collision(self, o):
        o.Kill(self.string)
        self.Kill(o.string)

        return False

    @property
    def string(self):
        return "Belladonna"