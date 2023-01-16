import wx

# ================================================================================
class TimedDialog(wx.Dialog):

    def __init__(self, *args, **kwargs):
        super(TimedDialog, self).__init__(*args, **kwargs)

        self.SetSize((400, 300))
        self.SetTitle('Please wait!')
        self.Centre()

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer)

        self.timer.Start(2000)  # 2 second interval

    def OnTimer(self, event):
        self.Close()


# ================================================================================
class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        self.SetSize((300, 200))
        self.SetTitle('app')
        self.Centre()
        self.btn = wx.Button(self, -1, "click Me")
        self.btn.Bind(wx.EVT_BUTTON, self.OnClicked)

    def OnClicked(self, event):
        dlg = TimedDialog(self)
        dlg.ShowModal()


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()