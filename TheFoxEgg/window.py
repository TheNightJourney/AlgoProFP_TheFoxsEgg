import wx

class FoxEggApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)
    
        self.InitFrame()
        
    def InitFrame(self):
        frame = FoxEggFrame(parent=None, title="The Fox's Egg", 
                            pos = (100, 100))
        frame.Center()
        frame.Show()
        
class FoxEggFrame(wx.Frame):
    def __init__(self, parent, title, pos):
        super().__init__(parent=parent, title=title, pos=pos,
        size=(750, 500))
        icon = wx.Icon('images/TFELogoPNG.png', wx.BITMAP_TYPE_ANY)
        self.SetIcon(icon)
        self.StartInit()
        
    def StartInit(self):
        panel = FoxEggPanel(parent=self)
        
class FoxEggPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.btn = wx.Button(self, -1, "Welcome to the Fox's Egg, and thank you for your patronage!")
        self.btn.Bind(wx.EVT_BUTTON, self.OnClicked)

    def OnClicked(self, event):
        self.Close()
