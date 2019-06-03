from Directions.Point import Point
from Directions.Navigation import Navigation
from Uti.Utilities import Utilities

import sys

class Board(object):
    """description of class"""

    def __init__(self, r, c):
        self.__row = r
        self.__col = c

        self.__organisms = []
        self.__seekBuffer = []

        for i in range(r * c):
            self.__organisms.append(None)

    @property
    def row(self):
        return self.__row

    @property
    def col(self):
        return self.__col

    def Validate(self, p):
        if (p.x < 0) or (p.y < 0) or (p.x >= self.row) or (p.y >= self.col):
            return False
        else:
            return True

    def SeekForFree(self, p):
        self.__seekBuffer.clear()

        x = 0 if p.x - 1 < 0 else p.x - 1
        y = 0 if p.y - 1 < 0 else p.y - 1

        yMax = p.x if p.x + 1 == self.row else p.x + 1
        xMax = p.y if p.y + 1 == self.col else p.y + 1

        for i in range(x, xMax + 1):
            for j in range(y, yMax + 1):

                if (i == p.x) and (j == p.y):
                    continue

                temp = Point(i, j)

                if self.__organisms[self.__index(temp)] == None:
                    self.__seekBuffer.append(temp)

        if len(self.__seekBuffer) == 0:
            return Navigation.NULL_POINT

        return self.__seekBuffer[Utilities.randomInt(0, len(self.__seekBuffer) - 1)]

    def SetAt(self, o):

        self.__seekBuffer.clear()

        for x in range(self.row):
            for y in range(self.col):
                
                temp = Point(x, y)

                if self.__organisms[self.__index(temp)] == None:
                    self.__seekBuffer.append(temp)

        if len(self.__seekBuffer) == 0:
            return

        if o.location != Navigation.NULL_POINT:
            self.__organisms[self.__index(o.location)] = None

        temp = self.__seekBuffer[Utilities.randomInt(0, len(self.__seekBuffer) - 1)]

        o.location = temp
        self.__organisms[self.__index(temp)] = o

    def SetAtPoint(self, p, o):
        if self.Validate(p) == False:
            return

        if o.location != Navigation.NULL_POINT:
            self.__organisms[self.__index(o.location)] = None

        o.location = p
        self.__organisms[self.__index(p)] = o

    def KillAt(self, p):
        self.__organisms[self.__index(p)] = None

    def GetAt(self, p):
        return self.__organisms[self.__index(p)]

    def __index(self, p):
        return p.y * self.row + p.x

    def Print(self):
        print("")
        print("")
        for i in range(self.row*self.col):
            o = self.__organisms[i]

            if i % self.col == 0:
                print("")

            if o == None:
                sys.stdout.write('N')
                sys.stdout.flush()
            else:
                sys.stdout.write(o.token)
                sys.stdout.flush()