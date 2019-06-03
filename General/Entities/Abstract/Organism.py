from Directions.Navigation import Navigation
from abc import ABC, abstractmethod, abstractproperty

class Organism(ABC):
    """description of class"""

    def __init__(self, s, i, a, w, t):
        self.__strength = s
        self.__initiative = i
        self.__age = a
        self.__location = Navigation.NULL_POINT
        self.__world = w
        self.__alive = True
        self.__token = t

    def Fight(self, o):
        if (self.strength < o.strength) == False:
            p = o.location
            o.Kill(self.string)
            self.Move(p)
        else:
            self.Kill(o.string)

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, p):
        self.__location = p

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        self.__strength = value

    @property
    def initiative(self):
        return self.__initiative

    @initiative.setter
    def initiative(self, value):
        self.__initiative = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value
        
    @property
    def token(self):
        return self.__token

    @abstractproperty
    def image(self):
        pass

    @property
    def world(self):
        return self.__world

    @world.setter
    def world(self, value):
        self.__world = value

    @property
    def isAlive(self):
        return self.__alive

    @abstractproperty
    def string(self):
        pass

    @abstractmethod
    def Action(self):
        pass

    @abstractmethod
    def Collision(self, o):
        pass

    @abstractmethod
    def Move(self, p):
        pass

    def Kill(self, s):
        self.__alive = False
        self.__world.Notify(s)
        self.__world.RemoveFromWorld(self)

    def buff(self, value):
        self.__strength += 3

    @staticmethod
    def compareTo(this, other):
        if this.initiative != other.initiative:
            if this.initiative > other.initiative:
                return 1
            else:
                return -1
        else:
            if this.age > other.age:
                return 1
            else:
                if this.age < other.age:
                    return -1
                else:
                    return 0