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
		primaryBoxSizer.Add( self.leftPartPanel, 3, wx.EXPAND |wx.ALL, 0 )

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


		self.rightPartPanel.SetSizer( gbSizer1 )
		self.rightPartPanel.Layout()
		gbSizer1.Fit( self.rightPartPanel )
		primaryBoxSizer.Add( self.rightPartPanel, 2, wx.EXPAND |wx.ALL, 0 )


		self.SetSizer( primaryBoxSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.UCBlogoBitmap.Bind( wx.EVT_PAINT, self.loadImage )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def loadImage( self, event ):
		event.Skip()


