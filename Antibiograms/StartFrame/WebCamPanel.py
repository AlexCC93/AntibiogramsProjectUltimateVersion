import wx
import cv2
import numpy as np
import os



class WebCamPanel(wx.Panel):
    
    def __init__(self, parent, camera, fps=10):
        # global mirror
        
        wx.Panel.__init__(self, parent)
        
        self.camera = camera
        return_value, frame = self.camera.read()
        height, width = frame.shape[:2]
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # if mirror:
        # 	frame = cv2.flip(frame, 1)
        
        self.bmp = wx.BitmapFromBuffer(width, height, frame)
        
        self.SetSize((width,height))
        
        self.timer = wx.Timer(self)
        self.timer.Start(1000./fps)
        
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_TIMER, self.NextFrame)
        
    def OnPaint(self, e):
        dc = wx.BufferedPaintDC(self)
        dc.DrawBitmap(self.bmp, 0, 0)
        
    def NextFrame(self, e):
        return_value, frame = self.camera.read()
        if return_value:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # if mirror:
            # 	frame = cv2.flip(frame, 1)
            self.bmp.CopyFromBuffer(frame)
            self.Refresh()