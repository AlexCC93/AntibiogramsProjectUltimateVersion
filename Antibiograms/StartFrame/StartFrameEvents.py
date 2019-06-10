#importing files
import wx
import os 
import random
#import the newly created GUI file
import StartFrameModule as SFM

class StartFrameEventsClass(SFM.StartFrameClass):    
    #constructor
    def __init__(self,parent):
        #initialize parent class
        SFM.StartFrameClass.__init__(self,parent)
    
    def RunHaloDetection(self, event):
        numHalos=random.randint(1,7)
        numAntibioticos=numHalos
        self.AntibioticsTextBox.SetValue(str(numAntibioticos))
        self.HalosTextBox.SetValue(str(numHalos))
        print numHalos

        