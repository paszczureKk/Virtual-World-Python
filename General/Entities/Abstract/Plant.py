from Organism import Organism
from Uti.Utilities import Utilities
from Directions.Navigation import Navigation
import Entities

class Plant(Organism):
    """description of class"""
    def __init__(self, s, a, w, p, t):
        Organism.__init__(self, s, 0, a, w, t)
        self.__probability = p

    def Action(self):

        if self.__probability < Utilities.randomFloat(0, 1):
            return

        p = self.world.SeekForFree(self.location)

        if p == Navigation.NULL_POINT:
            return

        org = Entities.Entities.CreateChar(self.token)

        if org != None:
            org.age = self.world.age
            org.world = self.world

            self.world.AddToWorld(org, p)
            self.world.Notify(self.string + " has grown on " + p.string)

    def Collision(self, o):

        self.Kill(o.string)

        o.Move(self.location)

        return False

    def Move(self, p):
        pass

    def Kill(self, s):
        Organism.Kill(self, self.string + " has been eaten by " + s)