from World import World
import wx

def main():

    __app = wx.App()

    w = World(__app)

    __app.MainLoop()

if __name__ == '__main__':
    main()