#importing files
import wx
import os 
#import the newly created GUI file
import StartFrameModule as SFM

class StartFrameEventsClass(SFM.StartFrameClass):    
    #constructor
    def __init__(self,parent):
        #initialize parent class
        SFM.StartFrameClass.__init__(self,parent)
    
   
        