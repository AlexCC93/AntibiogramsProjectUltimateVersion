#importing wx files
import wx
 
#import the newly created GUI file
import MainFrameModule as MFM

def scale_bitmapImage(bitmap, width, height):
    image = wx.ImageFromBitmap(bitmap)
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    result = wx.BitmapFromImage(image)
    return result   


class MainFrameEventsClass(MFM.MainFrameClass):
    #constructor
    def __init__(self,parent):
        #initialize parent class
        MFM.MainFrameClass.__init__(self,parent)
    
    def loadImage( self, event ):
        ImgInBitmap = wx.Bitmap(u"D:\Alex 2019\Antibiogramas\AntibiogramsProjectUltimateVersion\Images\logo.gif")
        New_Width=ImgInBitmap.GetWidth()*0.35
        New_Height=ImgInBitmap.GetHeight()*0.35
        ImgInBitmap = scale_bitmapImage(ImgInBitmap,New_Width,New_Height)
        self.UCBlogoBitmap = wx.StaticBitmap( self.logoContainerPanel, wx.ID_ANY, ImgInBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
    
     
