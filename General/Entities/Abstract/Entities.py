from enum import Enum
from Antelope import Antelope
from CyberSheep import CyberSheep
from Fox import Fox
from Sheep import Sheep
from Turtle import Turtle
from Wolf import Wolf
from Belladonna import Belladonna
from Dandelion import Dandelion
from Grass import Grass
from Guarana import Guarana
from HeracleumSosnowskyi import HeracleumSosnowskyi
from Human import Human

class Entities(Enum):
    """description of class"""

    antelope = 0
    cybersheep = 1
    fox = 2
    sheep = 3
    turtle = 4
    wolf = 5
    belladonna = 6
    dandelion = 7
    grass = 8
    guarana = 9
    heracleum = 10

    def Create(self):
        switcher = {
            0 : lambda : Antelope(),
            1 : lambda : CyberSheep(),
            2 : lambda : Fox(),
            3 : lambda : Sheep(),
            4 : lambda : Turtle(),
            5 : lambda : Wolf(),
            6 : lambda : Belladonna(),
            7 : lambda : Dandelion(),
            8 : lambda : Grass(),
            9 : lambda : Guarana(),
            10: lambda : HeracleumSosnowskyi(),
            }
        
        func = switcher.get(self.value, None)
        return func()

    @property
    def string(self):
        switcher = {
            0 : "Antelope",
            1 : "CyberSheep",
            2 : "Fox",
            3 : "Sheep",
            4 : "Turtle",
            5 : "Wolf",
            6 : "Belladonna",
            7 : "Dandelion",
            8 : "Grass",
            9 : "Guarana",
            10: "Heracleum",
            }
        
        return switcher.get(self.value, None)

    @staticmethod
    def CreateChar(t):
        switcher = {
            'A' : lambda : Antelope(),
            'C' : lambda : CyberSheep(),
            'F' : lambda : Fox(),
            'S' : lambda : Sheep(),
            'T' : lambda : Turtle(),
            'W' : lambda : Wolf(),
            'B' : lambda : Belladonna(),
            'D' : lambda : Dandelion(),
            'G' : lambda : Grass(),
            'U' : lambda : Guarana(),
            'H' : lambda : HeracleumSosnowskyi(),
            'P' : lambda : Human()
            }
        
        func = switcher.get(t, None)
        return func()

    @staticmethod
    def CreateString(s):
        switcher = {
            "Antelope" : lambda : Antelope(),
            "CyberSheep" : lambda : CyberSheep(),
            "Fox" : lambda : Fox(),
            "Sheep" : lambda : Sheep(),
            "Turtle" : lambda : Turtle(),
            "Wolf" : lambda : Wolf(),
            "Belladonna" : lambda : Belladonna(),
            "Dandelion" : lambda : Dandelion(),
            "Grass" : lambda : Grass(),
            "Guarana" : lambda : Guarana(),
            "Heracleum" : lambda : HeracleumSosnowskyi(),
            "Player" : lambda : Human()
            }
        
        func = switcher.get(s, None)
        return func()

