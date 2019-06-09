#importing files
import wx
import os 
#import the newly created GUI file
import MainFrameModule as MFM
from Antibiograms.StartFrame.StartFrameEvents import StartFrameEventsClass as SF


def scale_bitmapImage(bitmap, width, height):
    image = bitmap.ConvertToImage()
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    result = wx.Bitmap(image)
    return result   


class MainFrameEventsClass(MFM.MainFrameClass):    
    #constructor
    def __init__(self,parent):
        #initialize parent class
        MFM.MainFrameClass.__init__(self,parent)
    
    def loadImage( self, event ):
        relPath = "Images/logo.gif"
        imgPath = os.path.join(self.getProjectPath(), relPath)

        ImgInBitmap = wx.Bitmap(imgPath)
        New_Width=ImgInBitmap.GetWidth()*0.35
        New_Height=ImgInBitmap.GetHeight()*0.35
        ImgInBitmap = scale_bitmapImage(ImgInBitmap,New_Width,New_Height)
        self.UCBlogoBitmap = wx.StaticBitmap( self.logoContainerPanel, wx.ID_ANY, ImgInBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )

    def getProjectPath(self):
        fileDir = os.path.dirname(os.path.abspath(__file__))
        parentDir = os.path.dirname(fileDir)
        mainDir = os.path.dirname(parentDir)
        return mainDir

    def openStartFrame( self, event ):
        StartFrame=SF(self)                                      
        StartFrame.Show()

        