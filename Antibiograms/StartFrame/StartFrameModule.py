# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class StartFrameClass
###########################################################################

class StartFrameClass ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Anitbiogramas UCB", pos = wx.DefaultPosition, size = wx.Size( 1500,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		primaryBoxSizer = wx.BoxSizer( wx.HORIZONTAL )

		self.leftPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel4 = wx.Panel( self.leftPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		buttonContainerBS = wx.BoxSizer( wx.HORIZONTAL )

		self.CameraON_Button = wx.Button( self.m_panel4, wx.ID_ANY, u"Encender Cámara", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CameraON_Button.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		buttonContainerBS.Add( self.CameraON_Button, 0, wx.ALIGN_CENTER|wx.ALL, 0 )


		self.m_panel4.SetSizer( buttonContainerBS )
		self.m_panel4.Layout()
		buttonContainerBS.Fit( self.m_panel4 )
		bSizer2.Add( self.m_panel4, 1, wx.ALIGN_CENTER_HORIZONTAL, 0 )


		self.leftPanel.SetSizer( bSizer2 )
		self.leftPanel.Layout()
		bSizer2.Fit( self.leftPanel )
		primaryBoxSizer.Add( self.leftPanel, 1, wx.EXPAND |wx.ALL, 0 )

		self.rightPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel5 = wx.Panel( self.rightPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.startRecognitionButton = wx.Button( self.m_panel5, wx.ID_ANY, u"Comenzar detección de halos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.startRecognitionButton.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6.Add( self.startRecognitionButton, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.m_panel5.SetSizer( bSizer6 )
		self.m_panel5.Layout()
		bSizer6.Fit( self.m_panel5 )
		bSizer5.Add( self.m_panel5, 0, wx.EXPAND, 0 )


		self.rightPanel.SetSizer( bSizer5 )
		self.rightPanel.Layout()
		bSizer5.Fit( self.rightPanel )
		primaryBoxSizer.Add( self.rightPanel, 1, wx.EXPAND |wx.ALL, 0 )


		self.SetSizer( primaryBoxSizer )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


