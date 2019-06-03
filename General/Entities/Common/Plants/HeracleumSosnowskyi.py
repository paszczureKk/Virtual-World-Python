from Plant import Plant
from Animal import Animal
from ImageLoader import ImageLoader
import CyberSheep

class HeracleumSosnowskyi(Plant):
    """description of class"""
    
    def __init__(self, a = 0, w = None):
        if w == None:
            Plant.__init__(self, 10, 0, None, 0.01, 'H')
        else:
            Plant.__init__(self, 10, a, w, 0.01, 'H')

    @property
    def image(self):
        return ImageLoader.heracleum

    def Action(self):
        self.world.MassRemoveFromWorld(self.string, self.location,\
            lambda o : False if isinstance(o, Plant) or isinstance(o, CyberSheep.CyberSheep) else True)

        Plant.Action(self)

    def Collision(self, o):
        
        if not isinstance(o, CyberSheep.CyberSheep):
            o.Kill(self.string)
            self.Kill(o.string)
        else:
            Plant.Collision(self, o)

        return False

    @property
    def string(self):
        return "HeracleumSosnowskyi"