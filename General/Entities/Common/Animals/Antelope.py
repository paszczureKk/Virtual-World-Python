from Animal import Animal
from Uti.Utilities import Utilities
from Directions.Navigation import Navigation
from Directions.WorldDirections import WorldDirections
from ImageLoader import ImageLoader

class Antelope(Animal):
    """description of class"""

    __probability = 0.5

    def __init__(self, a = 0, w = None):
        if w == None:
            Animal.__init__(self, 4, 4, 0, None, 'A')
        else:
            Animal.__init__(self, 4, 4, a, w, 'A')

    @property
    def image(self):
        return ImageLoader.antelope

    def Action(self):
        for i in range(0, 2):
            if self.isAlive:
                Animal.Action(self)

    def Collision(self, o):
        if self.__probability < Utilities.randomFloat(0, 1):
            newP = Navigation.Translate(self.location, WorldDirections.DIR_NULL)

            self.Move(newP)

            return False

        return Animal.Collision(self, o)

    @property
    def string(self):
        return "Antelope"