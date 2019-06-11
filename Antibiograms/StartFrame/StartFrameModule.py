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
## Class StartFrame
###########################################################################

class StartFrame ( wx.Frame ):

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
		primaryBoxSizer.Add( self.leftPanel, 2, wx.EXPAND |wx.ALL, 0 )

		self.rightPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel5 = wx.Panel( self.rightPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.startRecognitionButton = wx.Button( self.m_panel5, wx.ID_ANY, u"Comenzar procesamiento", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.startRecognitionButton.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6.Add( self.startRecognitionButton, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.m_panel5.SetSizer( bSizer6 )
		self.m_panel5.Layout()
		bSizer6.Fit( self.m_panel5 )
		bSizer5.Add( self.m_panel5, 0, wx.EXPAND, 0 )

		bSizer61 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel51 = wx.Panel( self.rightPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel7 = wx.Panel( self.m_panel51, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText5 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Número de antibióticos detectados:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.AntibioticsTextBox = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.AntibioticsTextBox, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Número de halos detectados:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.HalosTextBox = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.HalosTextBox, 0, wx.ALL, 5 )


		self.m_panel7.SetSizer( fgSizer1 )
		self.m_panel7.Layout()
		fgSizer1.Fit( self.m_panel7 )
		bSizer7.Add( self.m_panel7, 3, wx.EXPAND |wx.ALL, 0 )

		self.m_panel8 = wx.Panel( self.m_panel51, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.editResultsButton = wx.Button( self.m_panel8, wx.ID_ANY, u"Editar resultados", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.editResultsButton, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.m_panel8.SetSizer( bSizer8 )
		self.m_panel8.Layout()
		bSizer8.Fit( self.m_panel8 )
		bSizer7.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 0 )


		self.m_panel51.SetSizer( bSizer7 )
		self.m_panel51.Layout()
		bSizer7.Fit( self.m_panel51 )
		bSizer61.Add( self.m_panel51, 1, wx.EXPAND |wx.ALL, 0 )


		bSizer61.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_panel6 = wx.Panel( self.rightPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		self.m_panel6.SetSizer( fgSizer3 )
		self.m_panel6.Layout()
		fgSizer3.Fit( self.m_panel6 )
		bSizer61.Add( self.m_panel6, 9, wx.EXPAND |wx.ALL, 5 )


		bSizer5.Add( bSizer61, 1, wx.EXPAND, 5 )


		self.rightPanel.SetSizer( bSizer5 )
		self.rightPanel.Layout()
		bSizer5.Fit( self.rightPanel )
		primaryBoxSizer.Add( self.rightPanel, 1, wx.EXPAND |wx.ALL, 0 )


		self.SetSizer( primaryBoxSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.startRecognitionButton.Bind( wx.EVT_BUTTON, self.RunProcess )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def RunProcess( self, event ):
		event.Skip()


