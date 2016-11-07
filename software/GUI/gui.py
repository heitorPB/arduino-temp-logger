try:
    # for Python2
    import Tkinter as tk
    from Tkinter import ttk
except ImportError:
    # for Python3
    import tkinter as tk
    from tkinter import ttk

from matplotlib.figure import Figure
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg


class TempLogger(tk.Frame):
    def __init__(self, master = None):
        ttk.Frame.__init__(self, master)
        self.master.title(u"Temperature and Humidity")
        self.pack()

        self.lastTemperature = tk.StringVar()
        self.lastHumidity    = tk.StringVar()
        self.lastTemperature.set(u"13.7 ºC")
        self.lastHumidity.set(   u"66.6 %")

        self._createWidgets()


    def _createWidgets(self):
        self.plot_area = ttk.Frame(self)
        self.plot_area.pack(side = 'top', fill = "both")

        self.user_area = ttk.Frame(self)
        self.user_area.pack(side = 'bottom', fill = 'x')

        # plot stuff
        # TODO add a second yaxis for RH
        # TODO add a nice style: http://matplotlib.org/examples/style_sheets/plot_fivethirtyeight.html
        fig = Figure()
        canvas = FigureCanvasTkAgg(fig, self.plot_area)
        canvas.draw()
        toolbar = NavigationToolbar2TkAgg(canvas, self.plot_area)
        toolbar.update()
        toolbar.pack(side="top")
        canvas.get_tk_widget().pack(side = "top", fill = "both", expand = True)

        graph = fig.add_subplot(1, 1, 1)
        graph.set_ylabel("Temperature $^\circ C$", size=18)
        graph.set_ylim(-20, 80)
        graph.grid()

        # buttons and labels stuff
        ## buttons
        self.buttons_area = ttk.Frame(self.user_area)
        self.buttons_area.pack(side = 'right', fill = 'y')
        self.buttons_area.rowconfigure(0, weight = 1, uniform = 1)
        self.buttons_area.rowconfigure(1, weight = 1, uniform = 1)

        self.startButton = ttk.Button(self.buttons_area, text = 'Start')
        self.stopButton  = ttk.Button(self.buttons_area, text = 'Stop', command = self.quit)
        self.startButton.grid(row = 0)
        self.stopButton.grid( row = 1)

        ## labels
        self.labels_area = ttk.Frame(self.user_area)
        self.labels_area.pack(side = 'left', fill = 'y')

        self.TempLabel = ttk.Label(self.labels_area, text = u"Current Temperature:")
        self.HumLabel  = ttk.Label(self.labels_area, text = u"Current Humidity:")
        self.TempLabel.grid(row = 0, sticky = 'W')
        self.HumLabel.grid( row = 1, sticky = 'W')

        self.lastTempLabel = ttk.Label(self.labels_area, textvariable = self.lastTemperature)
        self.lastHumLabel  = ttk.Label(self.labels_area, textvariable = self.lastHumidity)
        self.lastTempLabel.grid(row = 0, column = 1, sticky = 'W')
        self.lastHumLabel.grid( row = 1, column = 1, sticky = 'W')


def root_window(style = 'default'):
    window = tk.Tk()
    window.style = ttk.Style()
    if style in ttk.Style().theme_names():
        window.style.theme_use(style)
    else:
        print("Style", style, "does not exist, using default.")
        window.style.theme_use('default')

    window.style.configure("TLabel",  padding = 6, font = "Arial 12")
    window.style.configure("TButton", padding = 6, font = "Arial 12")

    return window