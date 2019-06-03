from Animal import Animal
from Directions.Navigation import Navigation
from Directions.WorldDirections import WorldDirections
from ImageLoader import ImageLoader

class Fox(Animal):
    """description of class"""
    
    def __init__(self, a = 0, w = None):
        if w == None:
            Animal.__init__(self, 3, 7, 0, None, 'F')
        else:
            Animal.__init__(self, 3, 7, a, w, 'F')

    @property
    def image(self):
       return ImageLoader.fox

    def Action(self):
        newP = Navigation.Translate(self.location, WorldDirections.DIR_NULL)

        if self.world.PointValidate(newP) == False:
            return
        
        o = self.world.GetAt(newP)

        if (o != None) and (self.strength < o.strength):
            return

        self.Move(newP)

    @property
    def string(self):
        return "Fox"