from Animal import Animal
from ImageLoader import ImageLoader
import HeracleumSosnowskyi
from Directions.WorldDirections import WorldDirections
from Directions.Navigation import Navigation

class CyberSheep(Animal):
    """description of class"""

    def __init__(self, a = 0, w = None):
        if w == None:
            Animal.__init__(self, 11, 4, 0, None, 'C')
        else:
            Animal.__init__(self, 11, 4, a, w, 'C')

        self.__target = None

    @property
    def image(self):
        return ImageLoader.cybersheep

    def Action(self):
        if self.__target == None:
            Animal.Action(self)
        else:
            self.Move(Navigation.Translate(self.location, self.__Translate()))

    def Collision(self, o):
        if isinstance(o, HeracleumSosnowskyi.HeracleumSosnowskyi):
            o.Kill(self.string)
            return False

        return Animal.Collision(self, o)
    
    @property
    def string(self):
        return "CyberSheep"

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        self.__target = value

    def __Translate(self):
        if self.location.x - self.target.x < 0:
            return WorldDirections.EAST
        else:
            if self.location.x - self.target.x > 0:
                return WorldDirections.WEST
            else:
                if self.location.y - self.target.y < 0:
                    return WorldDirections.SOUTH
                else:
                    if self.location.y - self.target.y > 0:
                        return WorldDirections.NORTH
                    else:
                        return WorldDirections.DIR_NULL