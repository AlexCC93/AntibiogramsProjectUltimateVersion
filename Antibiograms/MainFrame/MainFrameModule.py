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
## Class MainFrameClass
###########################################################################

class MainFrameClass ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Antibiogramas UCB ", pos = wx.DefaultPosition, size = wx.Size( 1500,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		primaryBoxSizer = wx.BoxSizer( wx.HORIZONTAL )

		self.leftPartPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.titleContainerPanel = wx.Panel( self.leftPartPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.title = wx.StaticText( self.titleContainerPanel, wx.ID_ANY, u"PROYECTO DE ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )

		self.title.SetFont( wx.Font( 35, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer4.Add( self.title, 1, wx.ALL, 5 )


		self.titleContainerPanel.SetSizer( bSizer4 )
		self.titleContainerPanel.Layout()
		bSizer4.Fit( self.titleContainerPanel )
		gbSizer2.Add( self.titleContainerPanel, wx.GBPosition( 15, 1 ), wx.GBSpan( 1, 4 ), wx.EXPAND |wx.ALL, 5 )

		self.titleContainerPanel2 = wx.Panel( self.leftPartPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.title2 = wx.StaticText( self.titleContainerPanel2, wx.ID_ANY, u"ANTIOBIOGRAMAS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title2.Wrap( -1 )

		self.title2.SetFont( wx.Font( 35, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer5.Add( self.title2, 0, wx.ALL, 5 )


		self.titleContainerPanel2.SetSizer( bSizer5 )
		self.titleContainerPanel2.Layout()
		bSizer5.Fit( self.titleContainerPanel2 )
		gbSizer2.Add( self.titleContainerPanel2, wx.GBPosition( 16, 3 ), wx.GBSpan( 1, 5 ), wx.EXPAND |wx.ALL, 5 )

		self.subtitleContainerPanel = wx.Panel( self.leftPartPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self.subtitleContainerPanel, wx.ID_ANY, u"Exactitud y rapidez en la elaboración de antibiogramas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6.Add( self.m_staticText4, 0, wx.ALL, 5 )


		self.subtitleContainerPanel.SetSizer( bSizer6 )
		self.subtitleContainerPanel.Layout()
		bSizer6.Fit( self.subtitleContainerPanel )
		gbSizer2.Add( self.subtitleContainerPanel, wx.GBPosition( 18, 1 ), wx.GBSpan( 1, 8 ), wx.EXPAND |wx.ALL, 5 )

		self.StartButtonPanel = wx.Panel( self.leftPartPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.StartButton = wx.Button( self.StartButtonPanel, wx.ID_ANY, u"COMENZAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.StartButton.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer7.Add( self.StartButton, 0, wx.ALL, 5 )


		self.StartButtonPanel.SetSizer( bSizer7 )
		self.StartButtonPanel.Layout()
		bSizer7.Fit( self.StartButtonPanel )
		gbSizer2.Add( self.StartButtonPanel, wx.GBPosition( 20, 3 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.InfoButtonPanel = wx.Panel( self.leftPartPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.InfoButton = wx.Button( self.InfoButtonPanel, wx.ID_ANY, u"Acerca de...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.InfoButton.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer8.Add( self.InfoButton, 0, wx.ALL, 5 )


		self.InfoButtonPanel.SetSizer( bSizer8 )
		self.InfoButtonPanel.Layout()
		bSizer8.Fit( self.InfoButtonPanel )
		gbSizer2.Add( self.InfoButtonPanel, wx.GBPosition( 20, 6 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )


		self.leftPartPanel.SetSizer( gbSizer2 )
		self.leftPartPanel.Layout()
		gbSizer2.Fit( self.leftPartPanel )
		primaryBoxSizer.Add( self.leftPartPanel, 8, wx.EXPAND |wx.ALL, 0 )

		self.rightPartPanel = wx.Panel( self, wx.ID_ANY, wx.Point( 0,1 ), wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.logoContainerPanel = wx.Panel( self.rightPartPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizerLogo = wx.BoxSizer( wx.HORIZONTAL )

		self.UCBlogoBitmap = wx.StaticBitmap( self.logoContainerPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerLogo.Add( self.UCBlogoBitmap, 1, wx.ALL, 5 )


		self.logoContainerPanel.SetSizer( bSizerLogo )
		self.logoContainerPanel.Layout()
		bSizerLogo.Fit( self.logoContainerPanel )
		gbSizer1.Add( self.logoContainerPanel, wx.GBPosition( 0, 30 ), wx.GBSpan( 20, 30 ), wx.EXPAND |wx.ALL, 0 )

		self.labelContainerPanel = wx.Panel( self.rightPartPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.IngMecLabel = wx.StaticText( self.labelContainerPanel, wx.ID_ANY, u"Ingeniería Mecatrónica", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.IngMecLabel.Wrap( -1 )

		self.IngMecLabel.SetFont( wx.Font( 25, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer3.Add( self.IngMecLabel, 1, wx.ALIGN_BOTTOM|wx.ALL, 5 )


		self.labelContainerPanel.SetSizer( bSizer3 )
		self.labelContainerPanel.Layout()
		bSizer3.Fit( self.labelContainerPanel )
		gbSizer1.Add( self.labelContainerPanel, wx.GBPosition( 36, 20 ), wx.GBSpan( 1, 40 ), wx.EXPAND |wx.ALL, 5 )


		self.rightPartPanel.SetSizer( gbSizer1 )
		self.rightPartPanel.Layout()
		gbSizer1.Fit( self.rightPartPanel )
		primaryBoxSizer.Add( self.rightPartPanel, 6, wx.EXPAND |wx.ALL, 0 )


		self.SetSizer( primaryBoxSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.StartButton.Bind( wx.EVT_BUTTON, self.openStartFrame )
		self.UCBlogoBitmap.Bind( wx.EVT_PAINT, self.loadImage )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def openStartFrame( self, event ):
		event.Skip()

	def loadImage( self, event ):
		event.Skip()


