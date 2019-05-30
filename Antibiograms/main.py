# -*- coding: utf-8 -*-


from MainFrame.mainFrame import MainFrame as MF
import wx

if __name__=='__main__':
    app=wx.App()                                        #app is an instance of the wx.App class, which initialize the wx GUI toolkit.
    frame=MF(None)                                      #Creates a frame. None means that this frame has no parent frame. 
                                                        #Second and third parameter are the name and size of the window.
    frame.Show()
    app.MainLoop()                                      #Start the application's MainLoop whose role is to handel events.





