import tkinter as tk
import time
t=-1
h,m,s,i=0,0,0,0
class Stopwatch(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()
    
    
    def createWidgets(self):
        self.Photo = tk.PhotoImage(file='stopwatch.gif')
        self.lbli = tk.Label(self,image=self.Photo)
        self.lbli.grid(row=2,column=0,columnspan=1)
        self.lbl1 = tk.Label(self,text="Stopwatch",width=25)
        self.lbl1.grid(row=0,column=0)
        self.lptm = tk.StringVar()
        self.llb = tk.Listbox(self,listvariable=self.lptm)
        self.llb.grid(row=2,column=1)
        self.tm = tk.StringVar()
        self.lbl2 = tk.Label(self,textvariable=self.tm)
        self.lbl2.grid(row=3,column=0,columnspan=1)
        self.stbtn = tk.Button(self,text="Start",width=25,command=self.start)
        self.stpbtn = tk.Button(self,text="Stop",width=25,command=self.stop)
        self.lpbtn = tk.Button(self,text="Lapse",width=25,command=self.lapse)
        self.rstbtn = tk.Button(self,text="Reset",state=tk.DISABLED,width=25,command=self.reset)
        self.stbtn.grid(row=4,column=0)
        self.stpbtn.grid(row=4,column=1)
        self.lpbtn.grid(row=5,column=0)
        self.rstbtn.grid(row=5,column=1)
    
    def update(self,h,m,s):
        self.tm.set('{}:{}:{}'.format(h,m,s))
        self.after(1000,self.start)
                    
    def start(self,event=None):
        global t
        global h,m,s
        if t==-1:
            h,m,s=0,0,0
            t+=2
            self.update(h,m,s)
            self.rstbtn['state']=tk.ACTIVE
            self.stbtn['state']=tk.DISABLED
        elif t==0:
            self.tm.set('{}:{}:{}'.format(h,m,s))
            t+=1
        else:
            t+=1
            self.stbtn['state']=tk.DISABLED
            if s>=59:
                m+=1
                s=0
                if m>=59:
                    h+=1
                    m=0
                    self.update(h,m,s)
                else:
                    self.update(h,m,s)
            else:
                s+=1
                self.update(h,m,s)

    def lapse(self):
        global h,m,s,i
        self.llb.insert(0,'{}:{}:{}'.format(h,m,s))

    def reset(self):
        global h,m,s
        self.tm.set('{}:{}:{}'.format(0,0,0))
        h,m,s=0,0,0
    def stop(self): 
        global t
        t=0
        self.stbtn['state']=tk.ACTIVE
                    

stpwch = Stopwatch()
stpwch.master.title("Sample Stopwatch")
stpwch.mainloop()
