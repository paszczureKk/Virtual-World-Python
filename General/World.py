from Layout import Layout
from Entities import Entities
from Directions.Navigation import Navigation
from Directions.Point import Point
from Board import Board
from Human import Human
from Organism import Organism
from Directions.Point import Point
from Directions.WorldDirections import WorldDirections
import wx
import CyberSheep
import HeracleumSosnowskyi

class World(object):
    """description of class"""

    def __init__(self, app):
        
        self.__organisms = []
        self.__born = []
        self.__dead = []
        self.__sheeps = []
        self.__heracleums = []
        self.__organismsC = 0
        self.__start = False
        self.__changed = False
        self.__layout = Layout(self, app)

    @property
    def age(self):
        self.__organismsC += 1
        return self.__organismsC

    @age.setter
    def age(self, value):
        self.__organismsC = value

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, value):
        self.__start = value

    @property
    def layout(self):
        return self.__layout
    
    @property
    def finish(self):
        return self.__player.isAlive

    @property
    def input(self):
        pass

    @input.setter
    def input(self, code):
        self.__player.input = code

    def __Populate(self, n):
        for i in range(n):
            for entity in Entities:
                o = entity.Create()
                #o = Entities.CreateString("Fox")
                o.age = self.age
                o.world = self
                self.AddToWorld(o, Navigation.NULL_POINT)

    def __ClearLegend(self):
        legend = self.layout.legend
        legend.Clear()

    def NextTurn(self):
        self.Notify("New turn!")

        if len(self.__born) != 0:
            for o in self.__born:
                self.__organisms.append(o)

            self.__born.clear()
            self.__born.sort(key = Organism.compareTo)

        for o in self.__organisms:
            if o.isAlive == True:
                o.Action()
        
        if len(self.__dead) != 0:
            for o in self.__dead:
                self.__organisms.remove(o)

            self.__dead.clear()

        if self.__changed == True:
            for sheep in self.__sheeps:
                p = self.__SeekClosest(sheep)
                sheep.target = p
            self.__change = False

    def __SeekClosest(self, sheep):
        if len(self.__heracleums) == 0:
            return None

        max = -1
        seek = None

        for heracleum in self.__heracleums:
            result = 0
            result += abs(sheep.location.x - heracleum.location.x)
            result += abs(sheep.location.y - heracleum.location.y)

            if (max == -1) or result < max:
                max = result
                seek = heracleum.location

        return seek

    def WorldInit(self, oc):

        rows = self.layout.height
        cols = self.layout.width

        self.__board = Board(cols, rows)

        self.__player = Human(self.age, self)
        self.AddToWorld(self.__player, Navigation.NULL_POINT)

        self.__Populate(oc)

    def Notify(self, s):
        self.__layout.Print(s)

    def AddToWorld(self, o, p):
        self.__born.append(o)

        if p == Navigation.NULL_POINT:
            self.__board.SetAt(o)
        else:
            self.__board.SetAtPoint(p, o)

        self.__layout.Update(o)

        if isinstance(o, CyberSheep.CyberSheep):
            self.__sheeps.append(o)
        if isinstance(o, HeracleumSosnowskyi.HeracleumSosnowskyi):
            self.__heracleums.append(o)
            self.__changed = True

    def RemoveFromWorld(self, o):
        self.__layout.Clear(o.location)
        self.__board.KillAt(o.location)
        self.__dead.append(o)

        if isinstance(o, CyberSheep.CyberSheep):
            self.__sheeps.remove(o)
        if isinstance(o, HeracleumSosnowskyi.HeracleumSosnowskyi):
            self.__heracleums.remove(o)
            self.__changed = True

    def MassRemoveFromWorld(self, s, p, foo):

        x = 0 if p.x - 1 < 0 else p.x - 1
        y = 0 if p.y - 1 < 0 else p.y - 1

        yMax = p.x if p.x + 1 == self.__board.row else p.x + 1
        xMax = p.y if p.y + 1 == self.__board.col else p.y + 1

        temp = Point(0, 0)

        for i in range(x, xMax + 1):
            for j in range(y, yMax + 1):
                if (i == p.x) and (y == p.y):
                    continue

                temp.set(i, j)

                o = self.__board.GetAt(temp)
                if o == None:
                    continue

                if foo(o) == False:
                    continue
                else:
                    o.Kill(s)

    def PointValidate(self, p):
        return self.__board.Validate(p)

    def SeekForFree(self, p):
        return self.__board.SeekForFree(p)

    def GetAt(self, p):
        return self.__board.GetAt(p)

    def MoveTo(self, p, o):
        self.__layout.Clear(o.location)
        self.__board.SetAtPoint(p, o)
        self.__layout.Update(o)

    def LegendUpdate(self, dir):
        self.__ClearLegend()
        
        legend = self.layout.legend

        legend.AppendText("STATISTICS:\n")
        legend.AppendText("Strength: " + str(self.__player.strength) + "\n")
        legend.AppendText("Position: " + self.__player.location.string + "\n")
        
        legend.AppendText("\n")
        
        if dir != WorldDirections.DIR_NULL:
            legend.AppendText("Current direction: " + Navigation.string(dir) + "\n")

        legend.AppendText("\n")

        legend.AppendText("Cooldown: " + str(self.__player.cooldown) + "\n")
        legend.AppendText("Duration: " + str(self.__player.duration) + "\n")

        if self.__player.duration > 0:
            legend.AppendText("\n")
            legend.AppendText("Player empowered.\n")

    def ClearInput(self):
        self.__direction = WorldDirections.DIR_NULL

    def Save(self, e):

        f = open("C:/Users/abc/source/repos/PythonApplication1/PythonApplication1/General/Resources/save.txt", "w")

        #saving
        self.Notify("Saving...")

        #world
        f.write("%d\n" %self.__organismsC)

        #board
        f.write("%d\n%d\n" %(self.__board.row, self.__board.col))

        p = Point(0, 0)

		#organisms
        for y in range(self.__board.row):
            for x in range(self.__board.col):
                p.set(x, y)
                o = self.GetAt(p)

                if o == None:
                     f.write("%d\n" %0)
                else:
                    f.write("%d\n%c\n%d\n%d\n" %(1, o.token, o.age, o.strength))

        #born
        f.write("%d\n" %len(self.__born))
        for o in self.__born:
            if o == None:
                f.write("%d\n" %0)
            else:
                f.write("%d\n%d\n%d\n" %(1, o.location.x, o.location.y))

        #dead
        f.write("%d\n" %len(self.__dead))
        for o in self.__dead:
            if o == None:
                f.write("%d\n" %0)
            else:
                f.write("%d\n%d\n%d\n" %(1, o.location.x, o.location.y))

        f.write("%d\n%d" %(self.__player.cooldown, self.__player.duration))

        f.close()
        self.Notify("Saving complete!")

    def Load(self, e):

        f = open("C:/Users/abc/source/repos/PythonApplication1/PythonApplication1/General/Resources/save.txt", "r")

        #loading
        self.Notify("Loading...")

        i1 = int(f.readline())
        self.age = i1

        #board
        i1 = int(f.readline())
        i2 = int(f.readline())

        self.layout.Build(i1, i2)

        self.__born.clear()
        self.__dead.clear()

        #organisms
        for y in range(self.__board.row):
            for x in range(self.__board.col):
                p = Point(x, y)

                i1 = int(f.readline())

                if i1 == 0:
                    continue
                else:
                    t = f.readline()[0]
                    i2 = int(f.readline())
                    i3 = int(f.readline())

                    o = Entities.CreateChar(t)
                    o.world = self
                    o.age = i2
                    o.strength = i3
                    o.location = p

                    self.AddToWorld(o, p)

        self.__board.Print()

        #born
        i1 = int(f.readline())
        for i in range(i1):
            i2 = int(f.readline())
            if i2 == 0:
                continue
            else:
                i3 = int(f.readline())
                i4 = int(f.readline())

                p = Point(i3, i4)

                self.__born.append(self.GetAt(p))

        #dead
        i1 = int(f.readline())
        for i in range(i1):
            i2 = int(f.readline())
            if i2 == 0:
                continue
            else:
                i3 = int(f.readline())
                i4 = int(f.readline())

                p = Point(i3, i4)

                self.__dead.append(self.GetAt(p))

        i1 = int(f.readline())
        i2 = int(f.readline())

        self.__player.SetActive(i1, i2)

        f.close()
        self.__ClearLegend()
        self.Notify("Loading complete!")