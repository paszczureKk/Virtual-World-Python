import wx

class ImageLoader(object):
    """description of class"""

    @staticmethod
    def LoaderInit():
        ImageLoader.background  = wx.Bitmap("C:/Users/abc/source/repos/PythonApplication1/PythonApplication1/General/Resources/background.png", wx.BITMAP_TYPE_ANY)

        ImageLoader.heracleum   = wx.Bitmap("C:/Users/abc/source/repos/PythonApplication1/PythonApplication1/General/Resources/heracleum.png", wx.BITMAP_TYPE_ANY)
        ImageLoader.guarana     = wx.Bitmap("C:/Users/abc/source/repos/PythonApplication1/PythonApplication1/General/Resources/guarana.png", wx.BITMAP_TYPE_ANY)
        ImageLoader.grass       = wx.Bitmap("C:/Users/abc/source/repos/PythonApplication1/PythonApplication1/General/Resources/grass.png", wx.BITMAP_TYPE_ANY)
        ImageLoader.dandelion   = wx.Bitmap("C:/Users/abc/source/repos/PythonApplication1/PythonApplication1/General/Resources/dandelion.png", wx.BITMAP_TYPE_ANY)
        ImageLoader.belladonna  = wx.Bitmap("C:/Users/abc/source/repos/PythonApplication1/PythonApplication1/General/Resources/belladonna.png", wx.BITMAP_TYPE_ANY)

        ImageLoader.antelope    = wx.Bitmap("C:/Users/abc/source/repos/PythonApplication1/PythonApplication1/General/Resources/antelope.png", wx.BITMAP_TYPE_ANY)
        ImageLoader.cybersheep  = wx.Bitmap("C:/Users/abc/source/repos/PythonApplication1/PythonApplication1/General/Resources/cybersheep.png", wx.BITMAP_TYPE_ANY)
        ImageLoader.fox         = wx.Bitmap("C:/Users/abc/source/repos/PythonApplication1/PythonApplication1/General/Resources/fox.png", wx.BITMAP_TYPE_ANY)
        ImageLoader.sheep       = wx.Bitmap("C:/Users/abc/source/repos/PythonApplication1/PythonApplication1/General/Resources/sheep.png", wx.BITMAP_TYPE_ANY)
        ImageLoader.turtle      = wx.Bitmap("C:/Users/abc/source/repos/PythonApplication1/PythonApplication1/General/Resources/turtle.png", wx.BITMAP_TYPE_ANY)
        ImageLoader.wolf        = wx.Bitmap("C:/Users/abc/source/repos/PythonApplication1/PythonApplication1/General/Resources/wolf.png", wx.BITMAP_TYPE_ANY)

        ImageLoader.player      = wx.Bitmap("C:/Users/abc/source/repos/PythonApplication1/PythonApplication1/General/Resources/player.png", wx.BITMAP_TYPE_ANY)