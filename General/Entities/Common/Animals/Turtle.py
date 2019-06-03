from Animal import Animal
from Uti.Utilities import Utilities
from ImageLoader import ImageLoader

class Turtle(Animal):
    """description of class"""

    __probability = 0.25
       
    def __init__(self, a = 0, w = None):
        if w == None:
            Animal.__init__(self, 2, 1, 0, None, 'T')
        else:
            Animal.__init__(self, 2, 1, a, w, 'T')

    @property
    def image(self):
        return ImageLoader.turtle

    def Action(self):
        if self.__probability < Utilities.randomFloat(0, 1):
            return

        Animal.Action(self)

    def Collision(self, o):
        if self.TypeCheck(o) == False:
            if o.strength < 5:
                return False

        return Animal.Collision(self, o)

    @property
    def string(self):
        return "Turtle"


