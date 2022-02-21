import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import pyplot as plt
from matplotlib import style
import time

import  tkinter as tk
from tkinter import ttk

from multiprocessing import Process, Queue
from DataGenerator import func

def GeneralFunction():

    LARGE_FONT = ("Verdana", 12)
    NORM_FONT = ("Verdana", 10)
    SMALL_FONT = ("Verdana", 8)
    style.use("tableau-colorblind10")


    f = Figure(figsize=(5, 5), dpi=80)
    a = f.add_subplot(111)


    def popupmsg(msg):
        popup = tk.Tk()
        popup.geometry('200x100+200+200')

        def leavemini():
            popup.destroy()

        popup.wm_title("!")
        ttk.Label(popup, text=msg, font=NORM_FONT).pack()
        ttk.Button(popup, text="OK", command=leavemini).pack()
        popup.mainloop()

    def pullData(adress = "sampleData.txt"):
        dataList = open(adress, "r").read().split('\n')
        xlist = []
        ylist = []
        for eachLine in dataList:
            if len(eachLine) > 1:
                x, y = eachLine.split(' ')
                xlist.append(int(x))
                ylist.append(int(y))
        return xlist, ylist

    def animate(i):
        xlist = []
        ylist = []
        while q.qsize() != 0:
            xlist.append(q.get()[0])
            ylist.append(q.get()[1])
        time.sleep(5)
        print(xlist)
        #a.clear()
        a.plot(xlist, ylist, ".")
        plt.show()


    class SeaofCMeas(tk.Tk):
        def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)
            tk.Tk.iconbitmap(self, default="icon.ico")
            tk.Tk.wm_title(self, "Cold DC Measurments")
           # tk.wm_colormapwindows(self, "blue")

            container = tk.Frame(self)
            container.pack(side="top", fill="both", expand=True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

            menubar = tk.Menu(container)
            filemenu = tk.Menu(menubar, tearoff=0)
            filemenu.add_command(label="Save settings", command=lambda: popupmsg("Not supported"))
            filemenu.add_separator()
            filemenu.add_command(label="Exit", command=quit)
            menubar.add_cascade(label="File", menu=filemenu)

            tk.Tk.config(self, menu=menubar)
            self.frames = {}

            for F in (StartPage, ShowPlot):

                frame = F(container, self)
                self.frames[F] = frame
                frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame(StartPage)

        def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()

    class StartPage(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = ttk.Label(self, text="Home", font=LARGE_FONT)
            label.pack(pady=10, padx=10)
            ttk.Button(self, text="Show plot",
                                 command=lambda: controller.show_frame(ShowPlot)).pack()


    class ShowPlot(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = ttk.Label(self, text="I-V", font=LARGE_FONT)
            label.pack(pady=10, padx=10)

            ttk.Button(self, text="Home",
                       command=lambda: controller.show_frame(StartPage)).pack()
            # ttk.Button(self, text="Generate Data",
            #             command=StartProc).pack()

            canvas = FigureCanvasTkAgg(f, self)
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)




    app = SeaofCMeas()
    app.geometry('700x600+10+10')
    ani = animation.FuncAnimation(f, animate, interval=1000)
    app.mainloop()


if __name__ == '__main__':
    q = Queue()
    process = Process(target = func, args = (q,))
    process.start()
    GeneralFunction()
