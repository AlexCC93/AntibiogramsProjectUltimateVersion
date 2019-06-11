#importing files
import wx
import os 
import random
#import the newly created GUI file
import StartFrameModule as SFM



class StartFrameEvents(SFM.StartFrame):  
    numHalos=0
    numAntibiotics=0  
    #constructor
    def __init__(self,parent):
        #initialize parent class
        SFM.StartFrame.__init__(self,parent)

    
    def RunProcess(self, event):
        self.RunHaloDetection()
        self.DrawResultsSection()

    
    def RunHaloDetection(self):
        numHalos=random.randint(1,7)
        numAntibiotics=numHalos
        self.AntibioticsTextBox.SetValue(str(numAntibiotics))
        self.HalosTextBox.SetValue(str(numHalos))
        print numHalos

    def DrawResultsSection(self):
        self.sections = numHalos
        for x in sections:
            print("hello im in grid sizer")
            label = "Halo %s" % x
            newLabel = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Halo %s" % x, wx.DefaultPosition, wx.DefaultSize, 0 )             
            self.fgSizer3.Add( newLabel, 0, wx.ALL, 5 )
