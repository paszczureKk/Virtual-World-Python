import wx
from Entities import Entities

class PopUpMenu(wx.Menu):
    """description of class"""

    def __init__(self, parent, w, index):
        super(PopUpMenu, self).__init__()

        self.__ids = []

        self.__index = index
        self.__world = w
        self.parent = parent

        for entity in Entities:
            id = wx.NewId()
            item = wx.MenuItem(self, id, entity.string)
            self.Append(item)
            self.__ids.append(id)
            self.Bind(wx.EVT_MENU, self.Create, item)


    def Create(self, e):

        id = e.GetId()
        index = self.__ids.index(id)

        o = Entities.CreateString(Entities(index).string)
        o.age = self.__world.age
        o.world = self.__world

        self.__world.AddToWorld(o, self.__index)

    def OnClose(self, e):
        self.parent.Close()