import calendar

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import pyplot as plt
from matplotlib import style

import  tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 14)
NORM_FONT = ("Verdana", 12)
SMALL_FONT = ("Verdana", 10)


plt.style.use("tableau-colorblind10")

f = Figure()
a = f.add_subplot(111)

colorStyle = {'1': "#e8ebf2", '2': "#a3b1bc", '3': "#4e606e", '4': "#1d242a"}

def popupmsg(msg):
    popup = tk.Tk()
    popup.geometry('170x70+100+100')

    def leavemini():
        popup.destroy()

    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.grid(column=0, row=0)
    B1 = ttk.Button(popup, text="OK", command=leavemini)
    B1.grid(column=0, row=2)
    popup.mainloop()

def animate(i):
    pullData = open("sampleData.txt", "r").read()
    dataList = pullData.split('\n')
    xlist = []
    x2list = []
    ylist = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xlist.append(int(x))
            ylist.append(int(y))
    a.clear()
    a.plot(xlist, ylist)

def createNewWindow():
    vv = tk.Tk()
    vv.geometry('700x500+300+10')
    canvas = FigureCanvasTkAgg(f, vv)
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, vv, pack_toolbar=True)
    toolbar.update()
    canvas.get_tk_widget().pack()
    canvas._tkcanvas.pack()


class SeaofCMeas(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="icon.ico")
        tk.Tk.wm_title(self, "Cold DC Measurments")
       # tk.wm_colormapwindows(self, "blue")

        container = tk.Frame(self)
        container.grid(column=0, row=0)
        # container.grid_rowconfigure((0, 1, 2), weight=1)
        # container.grid_columnconfigure(1, weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings", command=lambda: popupmsg("Not supported"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)

        st = ttk.Style()
        st.theme_use('alt')
        st.configure('W.TButton', relief="flat",  foreground=colorStyle['3'], background=colorStyle['2'],  borderwidth=3, font=NORM_FONT)
        st.map('W.TButton', background=[('active', colorStyle['4']), ('disabled', '#f0f0f0')])

        tk.Tk.config(self, menu=menubar)

        self.frames = {}

        for F in (StartPage, R_T, I_V, I_V_H, SMopen):

            frame = F(container, self)
            self.frames[F] = frame
            frame.configure(bg=colorStyle['1'])
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ttk.Label(self, text="Home", foreground=colorStyle['2'], background=colorStyle['1'],  font=LARGE_FONT).grid(column=0, row=0, ipady=3, ipadx=10)
        ttk.Separator(self, orient='horizontal').grid(column=0, row=0, sticky="SEW")
        ttk.Separator(self, orient='vertical').grid(column=1, row=1, rowspan=5, sticky="SEN")

        ttk.Button(self, text="Home", style='W.TButton',
                   command=lambda: controller.show_frame(StartPage)).grid(column=0, row=1, ipady=2, ipadx=10)
        ttk.Button(self, text="R(T)", style='W.TButton',
                   command=lambda: controller.show_frame(R_T)).grid(column=0, row=2, ipady=2, ipadx=10)
        ttk.Button(self, text="I-V", style='W.TButton',
                   command=lambda: controller.show_frame(I_V)).grid(column=0, row=3, ipady=2, ipadx=10)
        ttk.Button(self, text="I-V(ext)", style='W.TButton',
                   command=lambda: controller.show_frame(I_V_H)).grid(column=0, row=4, ipady=2, ipadx=10)
        ttk.Button(self, text="Show", style='W.TButton',
                   command=lambda: controller.show_frame(SMopen)).grid(column=0, row=5, ipady=2, ipadx=10)


class R_T(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #Первый столбец
        ttk.Label(self, text="R(T)", foreground=colorStyle['2'], background=colorStyle['1'],  font=LARGE_FONT).grid(column=0, row=0, ipady=3, ipadx=10, columnspan=2)
        ttk.Separator(self, orient='horizontal').grid(column=0, row=0, columnspan=2, sticky="SEW")

        ttk.Button(self, text="Home", style='W.TButton',
                   command=lambda: controller.show_frame(StartPage)).grid(column=0, row=1, ipady=2, ipadx=10)
        ttk.Button(self, text="R(T)", style='W.TButton',
                   command=lambda: controller.show_frame(R_T)).grid(column=0, row=2, ipady=2, ipadx=10)
        ttk.Button(self, text="I-V", style='W.TButton',
                   command=lambda: controller.show_frame(I_V)).grid(column=0, row=3, ipady=2, ipadx=10)
        ttk.Button(self, text="I-V(ext)", style='W.TButton',
                   command=lambda: controller.show_frame(I_V_H)).grid(column=0, row=4, ipady=2, ipadx=10)
        ttk.Button(self, text="Show", style='W.TButton',
                   command=lambda: controller.show_frame(SMopen)).grid(column=0, row=5, ipady=2, ipadx=10)

        # Второй столбец
        ttk.Label(self, text="Sample", foreground=colorStyle['2'], background=colorStyle['1'],  font=LARGE_FONT).grid(column=1, row=1, ipady=3, ipadx=10, sticky="SEW")
        ttk.Label(self, text="Current", foreground=colorStyle['2'], background=colorStyle['1'],  font=NORM_FONT).grid(column=1, row=2, ipady=3, ipadx=10, sticky="SEW")
        ttk.Label(self, text="Voltage", foreground=colorStyle['2'], background=colorStyle['1'], font=NORM_FONT).grid(column=1, row=3, ipady=3, ipadx=10, sticky="SEW")
        ttk.Separator(self, orient='horizontal').grid(column=1, row=3, sticky="SEW")


class I_V(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ttk.Label(self, text="I-V", foreground=colorStyle['2'], background=colorStyle['1'],  font=LARGE_FONT).grid(column=0, row=0, ipady=3, ipadx=10)

        ttk.Button(self, text="Home", style='W.TButton',
                   command=lambda: controller.show_frame(StartPage)).grid(column=0, row=1, ipady=2, ipadx=10)
        ttk.Button(self, text="R(T)", style='W.TButton',
                   command=lambda: controller.show_frame(R_T)).grid(column=0, row=2, ipady=2, ipadx=10)
        ttk.Button(self, text="I-V", style='W.TButton',
                   command=lambda: controller.show_frame(I_V)).grid(column=0, row=3, ipady=2, ipadx=10)
        ttk.Button(self, text="I-V(ext)", style='W.TButton',
                   command=lambda: controller.show_frame(I_V_H)).grid(column=0, row=4, ipady=2, ipadx=10)
        ttk.Button(self, text="Show", style='W.TButton',
                   command=lambda: controller.show_frame(SMopen)).grid(column=0, row=5, ipady=2, ipadx=10)


class I_V_H(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ttk.Label(self, text="Extended I-V", foreground=colorStyle['2'], background=colorStyle['1'],  font=LARGE_FONT).grid(column=0, row=0, ipady=3, ipadx=10)


        ttk.Button(self, text="Home", style='W.TButton',
                   command=lambda: controller.show_frame(StartPage)).grid(column=0, row=1, ipady=2, ipadx=10)
        ttk.Button(self, text="R(T)", style='W.TButton',
                   command=lambda: controller.show_frame(R_T)).grid(column=0, row=2, ipady=2, ipadx=10)
        ttk.Button(self, text="I-V", style='W.TButton',
                   command=lambda: controller.show_frame(I_V)).grid(column=0, row=3, ipady=2, ipadx=10)
        ttk.Button(self, text="I-V(ext)", style='W.TButton',
                   command=lambda: controller.show_frame(I_V_H)).grid(column=0, row=4, ipady=2, ipadx=10)
        ttk.Button(self, text="Show", style='W.TButton',
                   command=lambda: controller.show_frame(SMopen)).grid(column=0, row=5, ipady=2, ipadx=10)


class SMopen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ttk.Label(self, text="Show Plot", foreground=colorStyle['2'], background=colorStyle['1'], font=LARGE_FONT).grid(column=0, row=0, ipady=3, ipadx=10)

        ttk.Button(self, text="Home", style='W.TButton',
                   command=lambda: controller.show_frame(StartPage)).grid(column=0, row=1, ipady=2, ipadx=10)
        ttk.Button(self, text="R(T)", style='W.TButton',
                   command=lambda: controller.show_frame(R_T)).grid(column=0, row=2, ipady=2, ipadx=10)
        ttk.Button(self, text="I-V", style='W.TButton',
                   command=lambda: controller.show_frame(I_V)).grid(column=0, row=3, ipady=2, ipadx=10)
        ttk.Button(self, text="I-V(ext)", style='W.TButton',
                   command=lambda: controller.show_frame(I_V_H)).grid(column=0, row=4, ipady=2, ipadx=10)
        ttk.Button(self, text="Show", style='W.TButton',
                   command=lambda: controller.show_frame(SMopen)).grid(column=0, row=5, ipady=2, ipadx=10)

        ttk.Label(self, text="Enter file root", foreground=colorStyle['2'], background=colorStyle['1'], font=LARGE_FONT).grid(
            column=1, row=1, ipady=3, ipadx=10, sticky="SEW")
        ttk.Label(self, text="Folder", foreground=colorStyle['2'], background=colorStyle['1'], font=NORM_FONT).grid(
            column=1, row=2, ipady=3, ipadx=10, sticky="SEW")
        ttk.Label(self, text="Time", foreground=colorStyle['2'], background=colorStyle['1'], font=NORM_FONT).grid(
            column=1, row=3, ipady=3, ipadx=10, sticky="SEW")
        ttk.Separator(self, orient='horizontal').grid(column=1, row=3, sticky="SEW")


        #ttk.Entry(self, textvariable=fileroot).grid(column=2, row=1, ipady=2, ipadx=10)

        ttk.Button(self, text="Show Plot", style='W.TButton',
                   command=createNewWindow).grid(column=1, row=6, ipady=2, ipadx=10)


app = SeaofCMeas()
app.geometry('500x700+10+10')
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()


