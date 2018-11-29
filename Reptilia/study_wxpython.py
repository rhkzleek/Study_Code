#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import wx
import win32api
import sys,os

def test_0001():
    app = wx.App()
    frame = wx.Frame(None,-1,'Hello World!')
    frame.Show(True)
    app.MainLoop()

APP_TITLE = u'基本框架'
APP_ICON = 'python.ico'

class mainFrame(wx.Frame):
    '''
    程序主窗口类,继承自wx。Frame
    '''
    def __init__(self):
        '''
        构造函数
        '''
        wx.Frame.__init__(self,None,-1,APP_TITLE, style = wx.DEFAULT_FRAME_STYLE^wx.RESIZE_BORDER)
        #默认style是下列项的组合:wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN
        self.SetBackgroundColour(wx.Colour(1,1,1))
        self.SetSize((800,600))
        self.Center()

        #以下代码处理图标
        if hasattr(sys,'frozen') and getattr(sys,'frozen') == 'windows_exe':
            exeName = win32api.GetModuleFileName(win32api.GetModuleHandle(None))
            icon = wx.Icon(exeName,wx.BITMAP_TYPE_ICO)
        else:
            icon = wx.Icon(APP_ICON,wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        #以下添加各类控件
        wx.StaticText(self,-1,u'第一行输入框:',pos=(40,50),size=(100,100))
        wx.StaticText(self,-1,u'第二行输入框:',pos=(40,80),size=(100,100))

        self.tc1 = wx.TextCtrl(self,-1,'',poa=(145,50),size=(150,-100))
        self.tc2 = wx.TextCtrl(self,-1,'',pos=(145,80),size=(150,-100))

class mainApp(wx.App):
    def OnInit(self):
        self.SetAppName(APP_TITLE)
        self.Frame = mainFrame()
        self.Frame.Show()
        return True

if __name__ == '__main__':
    #test_0001()
    app = mainApp(redirect=True,filename='debug.txt')
    app.MainLoop()