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
        global numHalos
        numHalos=random.randint(1,7)
        numAntibiotics=numHalos
        self.AntibioticsTextBox.SetValue(str(numAntibiotics))
        self.HalosTextBox.SetValue(str(numHalos))
        # print numHalos

    def DrawResultsSection(self):
        sections = numHalos
        print(sections)
        for x in range(sections):
            print("hello im in grid sizer")
            cont=x+1
            label = "Halo %s" % cont
            newLabel = wx.StaticText(self.m_panel6, wx.ID_ANY, u"Halo %s" % cont, wx.DefaultPosition, wx.DefaultSize, 0 )             
            newLabel.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
            newLabel.Wrap( -1 )

            if x==0:
                fgSizer3 = wx.FlexGridSizer( 0, 4, 0, 0 )
                fgSizer3.SetFlexibleDirection( wx.BOTH )
                fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
            fgSizer3.Add( newLabel, 0, wx.ALL, 5 )    

            newTxtCtrl = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
            newTxtCtrl.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
            fgSizer3.Add( newTxtCtrl, 0, wx.ALL, 5 )
            if x==(sections-1):
                self.m_panel6.SetSizer( fgSizer3 )
                self.m_panel6.Layout()
                fgSizer3.Fit( self.m_panel6 )
            # calledSizer=self.GetSizer()

