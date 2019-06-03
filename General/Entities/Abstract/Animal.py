from Organism import Organism
from Directions.Navigation import Navigation
from Directions.WorldDirections import WorldDirections
import Entities

class Animal(Organism):
    """description of class"""
    def __init__(self, s, i, a, w, t):
        Organism.__init__(self, s, i, a, w, t)

    def Action(self):
        newP = Navigation.Translate(self.location, WorldDirections.DIR_NULL)

        if self.world.PointValidate(newP) == False:
            return

        self.Move(newP)

    def Collision(self, o):

        if self.TypeCheck(o):
            p = self.world.SeekForFree(self.location)

            if p == Navigation.NULL_POINT:
                return False

            org = Entities.Entities.CreateChar(self.token)

            if org != None:
                org.age = self.world.age
                org.world = self.world

                self.world.AddToWorld(org, p)
                self.world.Notify(self.string + " has been born on " + p.string)

            return False

        return True

    def Move(self, p):
        o = self.world.GetAt(p)

        if o == None:
            self.world.MoveTo(p, self)
        else:
            if o.Collision(self):
                if self.Collision(o):
                    self.Fight(o)

    def Kill(self, s):
        Organism.Kill(self, self.string + " has been slain by " + s)

    def TypeCheck(self, o):
        if isinstance(o, self.__class__):
            return True
        else:
            return False