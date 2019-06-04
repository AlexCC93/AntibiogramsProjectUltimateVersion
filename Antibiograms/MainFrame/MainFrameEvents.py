#importing wx files
import wx
 
#import the newly created GUI file
import MainFrameModule as MFM

class MainFrameEventsClass(MFM.MainFrameClass):
    #constructor
    def __init__(self,parent):
        #initialize parent class
        MFM.MainFrameClass.__init__(self,parent)

    def loadImage( self, event ):
        self.UCBlogoBitmap = wx.StaticBitmap( self.rightPartPanel, wx.ID_ANY, wx.Bitmap(u"D:\Alex 2019\Antibiogramas\AntibiogramsProjectUltimateVersion\Images\little.png", wx.BITMAP_TYPE_ANY), wx.Point( -1,-1 ), wx.DefaultSize, 0 )