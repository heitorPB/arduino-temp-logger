try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk


class TempLogger(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text = 'quit', command = self.quit)
        self.quitButton.grid()