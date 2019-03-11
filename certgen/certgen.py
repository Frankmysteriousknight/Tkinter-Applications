import io
import os
from tkinter import *
import tkinter as tk
import ttk
from tkinter import messagebox
from tkinter import filedialog
import datetime,xlrd
import PIL
from PIL import Image,ImageDraw,ImageTk
import pyautogui
filename = ''
i = 0
width = 300
height = 300
center = height//2
white = (255,255,255)
green = (0,128,0)
class CertGen(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        #All Frame
        self.mFrame = tk.Frame(self,width=500,height=500)
        self.mFrame.grid()
        self.certFrame = tk.Frame(self,width=500,height=500)
        #Main Frame
        CertGen.fname = tk.StringVar()
        self.sellbl = tk.Label(self.mFrame,text="Select Your Excel File")
        self.sellbl.grid(row=0,column=0,ipadx=25,pady=25)
        self.fnameti = tk.Entry(self.mFrame,textvariable=CertGen.fname)
        self.fnameti.grid(row=0,column=1,ipadx=10,pady=10)
        self.getfnb = tk.Button(self.mFrame,text="Choose File",command=self.Select)
        self.getfnb.grid(row=0,column=3,ipadx=10,pady=10)
        self.nextb = tk.Button(self.mFrame,text="Show",command=self.Show)
        self.nextb.grid(row=1,column=2,ipadx=10,pady=10)


        #Certificate Frame
        CertGen.name = tk.StringVar()
        CertGen.course = tk.StringVar()
        CertGen.prz = tk.StringVar()
        self.certCanvas = tk.Canvas(self.certFrame,width=800,height=800)
        self.certCanvas.grid(row=1,column=2)
        self.certimg = tk.PhotoImage(file='newcert.png')
        self.id = self.certCanvas.create_image(300,300,image=self.certimg)
        self.sepcertframe = ttk.Separator(self.certFrame,orient=tk.VERTICAL)
        self.sepcertframe.grid(row=0,column=1)
        self.ntid = self.certCanvas.create_text(300,340,text="Name")
        self.ctid = self.certCanvas.create_text(300,410,text="Course")
        self.dtid = self.certCanvas.create_text(420,490,text="Date")
        self.certmin = tk.Frame(self.certFrame)
        self.certmin.grid(row=0,column=1)
        self.prb = tk.Button(self.certmin,text="Print",command=self.Print)
        self.nb = tk.Button(self.certmin,text="Next",command=self.Next)
        self.prb.grid(row=0,column=0,ipadx=10,pady=10)
        self.nb.grid(row=0,column=2,ipadx=10,pady=10)

    def Select(self,event=None):
        global filename
        filename = filedialog.askopenfilename()
        self.fname.set(filename)

    def Show(self,event=None):
        self.mFrame.grid_forget()
        self.certFrame.grid()
    def Print(self,event=None):
        global i
        imag = pyautogui.screenshot("cert{}.pdf".format(i),(200,180,660,520))

    def Next(self,event=None):
        global filename,i
        i=i+1
        loc = filename
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        if i == sheet.nrows:
            messagebox.showinfo("INFO","There are no more candidates to generate Certificate")
            self.certFrame.grid_forget()
            self.mFrame.grid()
        else:
            name = sheet.cell_value(i,0)
            course = sheet.cell_value(i,2)
            dt = sheet.cell_value(i,1)
            cdt = datetime.datetime(*xlrd.xldate_as_tuple(dt,wb.datemode))
            course_date = str(cdt.day)+'-'+str(cdt.month)+'-'+str(cdt.year)
            self.certCanvas.itemconfigure(self.ctid,text=course)
            self.certCanvas.itemconfigure(self.ntid,text=name)
            self.certCanvas.itemconfigure(self.dtid,text=course_date)
        


certgen = CertGen()
certgen.master.geometry("900x900+80+80")
certgen.master.title("Certificate Generator")
certgen.mainloop()
