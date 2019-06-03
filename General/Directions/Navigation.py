from Directions.Point import Point
from Uti.Utilities import Utilities
from Directions.WorldDirections import WorldDirections

class Navigation(object):
    """description of class"""

    @staticmethod
    def NavigationInit():
        Navigation.NULL_POINT = Point(-1, -1)

    @staticmethod
    def Translate(p, dir):
        if dir == WorldDirections.DIR_NULL:
            dir = WorldDirections(Utilities.randomInt(0, WorldDirections.DIRECTIONS_COUNT.value - 1));

        x = p.x
        y = p.y

        point = Point(x, y)
        
        switcher = {
            WorldDirections.NORTH : lambda a, b : (a, b - 1),
            WorldDirections.EAST  : lambda a, b : (a + 1, b),
            WorldDirections.SOUTH : lambda a, b : (a, b + 1),
            WorldDirections.WEST  : lambda a, b : (a - 1, b)
            }
        
        func = switcher.get(dir, lambda a, b : (a, b))
        x, y = func(x, y)
        point.set(x, y)

        return point

    @staticmethod
    def string(dir):

        switcher = {
            WorldDirections.NORTH : "North",
            WorldDirections.EAST  : "East",
            WorldDirections.SOUTH : "South",
            WorldDirections.WEST  : "West"
            }
        
        return switcher.get(dir, "")
