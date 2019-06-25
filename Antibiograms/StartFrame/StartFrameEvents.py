#importing files
import wx
import os 
import random
#import the newly created GUI file
import StartFrameModule as SFM
from StartFrame.WebCamPanel import WebCamPanel
import numpy as np
import cv2

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
        self.results_sectionPanel.DestroyChildren()
        for x in range(sections):
            cont=x+1
            label = "Halo %s" % cont
            newLabel = wx.StaticText(self.results_sectionPanel, wx.ID_ANY, u"Halo %s" % cont, wx.DefaultPosition, wx.DefaultSize, 0 )             
            newLabel.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
            newLabel.Wrap( -1 )

            if x==0:
                results_sectionSizer = wx.FlexGridSizer( 0, 4, 0, 0 )
                results_sectionSizer.SetFlexibleDirection( wx.BOTH )
                results_sectionSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
            results_sectionSizer.Add( newLabel, 0, wx.ALL, 5 )

            newTxtCtrl = wx.TextCtrl( self.results_sectionPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
            newTxtCtrl.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
            results_sectionSizer.Add( newTxtCtrl, 0, wx.ALL, 5 )
            if x==(sections-1):
                self.results_sectionPanel.SetSizer( results_sectionSizer )
                self.results_sectionPanel.Layout()
                results_sectionSizer.Fit( self.results_sectionPanel )
            # calledSizer=self.GetSizer()

    def StartCamera( self, event ):
        self.leftPanel.DestroyChildren()
        camera = cv2.VideoCapture(1)
        camera.set(3, 720)
        camera.set(4, 780)
        self.leftPanel = WebCamPanel(self, camera) 

        
        # camera = cv2.Videocamerature(0)
        # while(True):
        #     # camerature frame-by-frame
        #     ret, frame = camera.read()

        #     # Our operations on the frame come here
            

        #     # Display the resulting frame
        #     cv2.imshow('frame',frame)
        #     if cv2.waitKey(1) & 0xFF == ord('q'):
        #         break

        # # When everything done, release the camerature
        # camera.release()
        # cv2.destroyAllWindows()
        # event.Skip()

