from Animal import Animal
from Directions.WorldDirections import WorldDirections
from Directions.Navigation import Navigation
from InputEnum import InputEnum
from ImageLoader import ImageLoader
import wx

class Human(Animal):
    """description of class"""

    def __init__(self, a = 0, w = None):

        if w == None:
            Animal.__init__(self, 5, 4, 0, None, 'P')
        else:
            Animal.__init__(self, 5, 4, a, w, 'P')
        
        self.__cooldown = 0
        self.__active = 0

        self.__control = WorldDirections.DIR_NULL

    @property
    def image(self):
       return ImageLoader.player

    def Action(self):
        self.world.LegendUpdate(WorldDirections.DIR_NULL)

        self.__CoolDown()
        self.Move(Navigation.Translate(self.location, self.__ControlParse(self.__control)))

        self.__ActiveDown()

        self.world.LegendUpdate(WorldDirections.DIR_NULL)

    def Collision(self, o):
        if self.duration > 0:
            o.Move(Navigation.Translate(self.location, WorldDirections.DIR_NULL))

            return False

        return True

    @property
    def string(self):
        return "Player"

    @property
    def cooldown(self):
        return self.__cooldown

    @property
    def duration(self):
        return self.__active

    def SetActive(self, cd, dur):
        self.__active = dur
        self.__cooldown = cd

    @property
    def input(self):
        return self.__control

    @input.setter
    def input(self, value):
        switcher = {
        wx.WXK_LEFT  : InputEnum.LEFT,
        wx.WXK_RIGHT : InputEnum.RIGHT,
        wx.WXK_DOWN  : InputEnum.DOWN,
        wx.WXK_UP    : InputEnum.UP,
        }

        self.__control = switcher.get(value, self.__control)
        self.__changed = True

        if value == wx.WXK_SPACE:
            self.__Special()

        self.world.LegendUpdate(self.__ControlParse(self.__control))

    def __CoolDown(self):
        if self.cooldown > 0:
            self.__cooldown -= 1

    def __ActiveDown(self):
        if self.duration > 0:
            self.__active -= 1
            if self.duration == 0:
                self.__cooldown = 5

    def __Special(self):
        if (self.duration > 0) or (self.cooldown > 0):
            return

        self.__active = 5

    def __ControlParse(self, ie):
        if ie == None:
            return WorldDirections.DIR_NULL

        switcher = {
            InputEnum.LEFT : WorldDirections.WEST,
            InputEnum.RIGHT : WorldDirections.EAST,
            InputEnum.UP : WorldDirections.NORTH,
            InputEnum.DOWN : WorldDirections.SOUTH
            }
        
        return switcher.get(ie, WorldDirections.DIR_NULL)


