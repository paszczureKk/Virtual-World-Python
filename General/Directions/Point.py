class Point(object):
    """description of class"""

    def __init__(self, x, y):
        self.set(x, y)

    def __eq__(self, other):
        if isinstance(other, Point):
            if self.x == other.x and self.__y == other.y:
                return True
            else:
                return False
        else:
            return False

    @property
    def string(self):
        return "(" + str(self.x) + " , " + str(self.y) +")"

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def set(self, x, y):
        self.__x = x
        self.__y = y