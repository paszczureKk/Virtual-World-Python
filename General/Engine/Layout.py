import wx
from ImageLoader import ImageLoader
import wx.lib.scrolledpanel as scrolled
from Directions.Point import Point
from PopUpMenu import PopUpMenu
from Directions.Navigation import Navigation

class Layout(object):
    """description of class"""
    
    def __init__(self, w, app):
        
        app.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.__world = w

        self.__frame = wx.Frame(None, title = "Virtual World Python, Daniel Szynszecki 175683", size = (800,200))
        
        self.__InitUI()
        self.__frame.Centre()

        self.__frame.Show()

    def __InitUI(self):

        ImageLoader.LoaderInit()
        Navigation.NavigationInit()

        self.__buttons = []
        self.__ids = []

        self.__menubar = wx.MenuBar()
        self.__fileMenu = wx.Menu()
        self.__fileItemQ = self.__fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        self.__fileItemL = self.__fileMenu.Append(wx.ID_OPEN, 'Load', 'Load application')

        self.__menubar.Append(self.__fileMenu, '&File')
        self.__frame.SetMenuBar(self.__menubar)

        self.__frame.Bind(wx.EVT_MENU, self.OnQuit, self.__fileItemQ)
        self.__frame.Bind(wx.EVT_MENU, self.__world.Load, self.__fileItemL)

        
        self.__panel = wx.Panel(self.__frame)
        self.__panel.SetBackgroundColour("white")

        self.__vbox = wx.BoxSizer(wx.VERTICAL)

        self.__hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.__st1 = wx.StaticText(self.__panel, label='Set border dimensions')
        self.__tc  = wx.TextCtrl(self.__panel)

        self.__hbox.Add(self.__st1, flag=wx.RIGHT, border=8)
        self.__hbox.Add(self.__tc, proportion = 1)

        self.__vbox.Add(self.__hbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        self.__btn = wx.Button(self.__panel, wx.ID_STOP, 'Done', (70, 30))
        self.__vbox.Add(self.__btn, flag=wx.ALIGN_CENTRE|wx.TOP, border = 30)

        self.__frame.Bind(wx.EVT_BUTTON, self.__Done, id = wx.ID_STOP)

        self.__panel.SetSizer(self.__vbox)


    def OnQuit(self, e):
        self.__frame.Close()

    def __Done(self, e):
        value = self.__tc.GetLineText(0)
        row, col = value.split(" ")
        row = int(row)
        col = int(col)
        self.Build(row, col)
        self.__world.start = True
        self.__world.WorldInit(2)

    def Build(self, row, col):

        self.__ids.clear()
        self.__buttons.clear()

        self.__width = col
        self.__height = row

        self.__frame.Destroy()

        self.__frame = wx.Frame(None, title = "Virtual World Python, Daniel Szynszecki 175683", size = (1000,1000))
        
        self.__menubar = wx.MenuBar()
        self.__fileMenu = wx.Menu()
        self.__fileItemQ = self.__fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        self.__fileItemS = self.__fileMenu.Append(wx.ID_SAVE, 'Save', 'Save application')
        self.__fileItemL = self.__fileMenu.Append(wx.ID_OPEN, 'Load', 'Load application')

        self.__menubar.Append(self.__fileMenu, '&File')
        self.__frame.SetMenuBar(self.__menubar)

        self.__frame.Bind(wx.EVT_MENU, self.OnQuit, self.__fileItemQ)
        self.__frame.Bind(wx.EVT_MENU, self.__world.Save, self.__fileItemS)
        self.__frame.Bind(wx.EVT_MENU, self.__world.Load, self.__fileItemL)

        self.__panel = wx.Panel(self.__frame)
        self.__panel.SetBackgroundColour("white")

        self.__game = scrolled.ScrolledPanel(self.__panel, -1, 
                                 style = wx.TAB_TRAVERSAL|wx.SUNKEN_BORDER)
        self.__game.SetAutoLayout(1)
        self.__game.SetupScrolling()

        self.__grid = wx.GridSizer(col, row, 2, 2)

        for i in range(row*col):
            self.__ids.append(wx.NewId())
            btn = wx.BitmapButton(self.__game, style = wx.EXPAND, size = (140,140), bitmap = ImageLoader.background, id = self.__ids[i])
            btn.SetLabel("null")
            self.__buttons.append(btn)
            self.__grid.Add(btn)

        self.__game.SetSizer(self.__grid)

        
        self.__vbox = wx.BoxSizer(wx.VERTICAL)
        self.__vbox.Add(self.__game, 8, wx.EXPAND)

        self.__console = wx.TextCtrl(self.__panel, style = wx.TE_MULTILINE)

        self.__vbox.Add(self.__console, 2, wx.EXPAND)

        self.__hbox = wx.BoxSizer(wx.HORIZONTAL)


        self.__hbox.Add(self.__vbox, 7, wx.EXPAND)

        self.__legendContainer = wx.BoxSizer(wx.VERTICAL)
        self.__legend = wx.TextCtrl(self.__panel, style = wx.TE_MULTILINE)

        self.__legendContainer.Add(self.__legend, 9, wx.EXPAND)

        self.__nextBtn = wx.Button(self.__panel, wx.ID_CANCEL, 'Next Turn', (70, 30))

        self.__legendContainer.Add(self.__nextBtn, 1, wx.CENTRE)

        self.__hbox.Add(self.__legendContainer, 3, wx.EXPAND)

        self.__panel.SetSizer(self.__hbox)

        self.__frame.Bind(wx.EVT_BUTTON, self.__NextTurn, id = wx.ID_CANCEL)

        for i in range(row*col):
            self.__frame.Bind(wx.EVT_BUTTON, self.__Create, id = self.__ids[i])

        self.__frame.Centre()
        self.__frame.Show()

    def __NextTurn(self, e):
        self.__world.NextTurn()

    def __Create(self, e):
        btn = e.GetEventObject()

        if btn.GetLabel() == "null":
            pos = wx.DefaultPosition
            menu = PopUpMenu(self.__frame, self.__world, self.__GetButtonIndex(btn))
            self.__frame.PopupMenu(menu, pos)

    def OnKeyDown(self, e):

        print("work")

        if (self.__world.start == False):
            e.Skip()
            return
    
        keycode = e.GetKeyCode()
    
        if (keycode == wx.WXK_LEFT) or (keycode == wx.WXK_RIGHT) or (keycode == wx.WXK_DOWN) or (keycode == wx.WXK_UP) or (keycode == wx.WXK_SPACE):
            self.__world.input = keycode

    def __GetIndex(self, p):
        return p.y * self.__width + p.x

    def __GetButtonIndex(self, b):
        p = Point(0, 0)
        index = self.__buttons.index(b)
        
        p.x = index % self.__width
        p.y = index // self.__width

        return p

    def Update(self, o):
        btn = self.__buttons[self.__GetIndex(o.location)]

        btn.SetBitmap(o.image)
        btn.SetLabel(o.string)
        btn.Refresh()

    def Clear(self, p):
        btn = self.__buttons[self.__GetIndex(p)]

        btn.SetBitmap(ImageLoader.background)
        btn.SetLabel("null")

    @property
    def legend(self):
        return self.__legend

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def Print(self, s):
        self.__console.AppendText(s + '\n')

