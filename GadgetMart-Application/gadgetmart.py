from tkinter import *
import tkinter as tk
import pymysql as sql
from tkinter import messagebox
import datetime
import smtplib as sp

loggedUser = ''
now = datetime.datetime.now()
today = str(now.year)+'-'+str(now.month)+'-'+str(now.day)
class Gadmart(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        #All Frames
        self.mFrame = tk.Frame(self)
        self.logFrame = tk.Frame(self.mFrame)
        self.sigFrame = tk.Frame(self.mFrame,width=500,height=500)
        self.hFrame = tk.Frame(self.mFrame)
        self.mFrame.grid()
        self.logFrame.grid()
        
        #Login Frame Widgets
        Gadmart.user = tk.StringVar()
        Gadmart.pas = tk.StringVar()
        self.gdlbl = tk.Label(self.logFrame,text="Gadget Market",font=('Comic Sans','30','bold'))
        self.gdlbl.grid(row=0,column=0,ipadx=25,pady=25)
        self.ulbl = tk.Label(self.logFrame,text="Username",font=('Comic Sans','20'))
        self.ulbl.grid(row=1,column=0,ipadx=10,pady=10)
        self.plbl = tk.Label(self.logFrame,text="Password",font=('Comic Sans','20'))
        self.plbl.grid(row=2,column=0,ipadx=10,pady=10)
        self.unt = tk.Entry(self.logFrame,textvariable=Gadmart.user)
        self.unt.grid(row=1,column=1,ipadx=10,pady=10)
        self.pnt = tk.Entry(self.logFrame,textvariable=Gadmart.pas,show='*')
        self.pnt.grid(row=2,column=1,ipadx=10,pady=10)
        self.logb = tk.Button(self.logFrame,text="Login",command=self.login)
        self.logb.grid(row=3,column=0,ipadx=30,pady=20)
        self.sigb = tk.Button(self.logFrame,text="SignUp",command=self.signup)
        self.sigb.grid(row=3,column=1,ipadx=30,pady=20)
        
        #SignUp Frame Widgets
        #Labels
        self.sglbl = tk.Label(self.sigFrame,text="SignUp Here",font=('Comic Sans','30','bold'))
        self.sglbl.grid(row=0,column=0,ipadx=25,pady=25)
        self.ulbl = tk.Label(self.sigFrame,text="Username",font=('Comic Sans','20'))
        self.ulbl.grid(row=1,column=0,ipadx=10,pady=10)
        self.fnlbl = tk.Label(self.sigFrame,text="First Name",font=('Comic Sans','20'))
        self.fnlbl.grid(row=2,column=0,ipadx=10,pady=10)
        self.lnlbl = tk.Label(self.sigFrame,text="Last Name",font=('Comic Sans','20'))
        self.lnlbl.grid(row=3,column=0,ipadx=10,pady=10)
        self.doblbl = tk.Label(self.sigFrame,text="Date of Birth",font=('Comic Sans','20'))
        self.doblbl.grid(row=4,column=0,ipadx=10,pady=10)
        self.adlbl = tk.Label(self.sigFrame,text="Address",font=('Comic Sans','20'))
        self.adlbl.grid(row=5,column=0,ipadx=10,pady=10)
        self.pnlbl = tk.Label(self.sigFrame,text="Phone No.",font=('Comic Sans','20'))
        self.pnlbl.grid(row=6,column=0,ipadx=10,pady=10)
        self.elbl = tk.Label(self.sigFrame,text="Email",font=('Comic Sans','20'))
        self.elbl.grid(row=7,column=0,ipadx=10,pady=10)
        self.pslbl = tk.Label(self.sigFrame,text="Password",font=('Comic Sans','20'))
        self.pslbl.grid(row=8,column=0,ipadx=10,pady=10)
        self.rpslbl = tk.Label(self.sigFrame,text="Re-Enter Password",font=('Comic Sans','20'))
        self.rpslbl.grid(row=9,column=0,ipadx=10,pady=10)
           
        #Entry 
        Gadmart.User = tk.StringVar()
        Gadmart.fname = tk.StringVar()
        Gadmart.lname = tk.StringVar()
        Gadmart.dob = tk.StringVar()
        Gadmart.ad = tk.StringVar()
        Gadmart.pn = tk.StringVar()
        Gadmart.e = tk.StringVar()
        Gadmart.p = tk.StringVar()
        Gadmart.rp = tk.StringVar()
        self.uent = tk.Entry(self.sigFrame,textvariable=Gadmart.User)
        self.uent.grid(row=1,column=1,ipadx=10,pady=10)
        self.fent = tk.Entry(self.sigFrame,textvariable=Gadmart.fname)
        self.fent.grid(row=2,column=1,ipadx=10,pady=10)
        self.lent = tk.Entry(self.sigFrame,textvariable=Gadmart.lname)
        self.lent.grid(row=3,column=1,ipadx=10,pady=10)
        self.dent = tk.Entry(self.sigFrame,textvariable=Gadmart.dob)
        self.dent.grid(row=4,column=1,ipadx=10,pady=10)
        self.aent = tk.Entry(self.sigFrame,textvariable=Gadmart.ad)
        self.aent.grid(row=5,column=1,ipadx=10,pady=10)
        self.pent = tk.Entry(self.sigFrame,textvariable=Gadmart.pn)
        self.pent.grid(row=6,column=1,ipadx=10,pady=10)
        self.eent = tk.Entry(self.sigFrame,textvariable=Gadmart.e)
        self.eent.grid(row=7,column=1,ipadx=10,pady=10)
        self.psent = tk.Entry(self.sigFrame,textvariable=Gadmart.p,show='*')
        self.psent.grid(row=8,column=1,ipadx=10,pady=10)
        self.rpsent = tk.Entry(self.sigFrame,textvariable=Gadmart.rp,show='*')
        self.rpsent.grid(row=9,column=1,ipadx=10,pady=10)
            
        #Buttons
        self.sigbtn = tk.Button(self.sigFrame,text="SignUp",font=('Comic Sans','20'),command=self.sign)
        self.sigbtn.grid(row=10,column=1,ipadx=10,pady=10)
        
        #Home Frame Widgets
        self.welbl = tk.Label(self.hFrame,text="Welcome",font=('Comic Sans','30','bold'))
        self.welbl.grid(row=0,column=0,ipadx=10,pady=10)
        self.lgbtn = tk.Button(self.hFrame,text="LOGOUT",command=self.logout)
        self.lgbtn.grid(row=0,column=5,ipadx=10,pady=10)
        
        #Product 1
        self.imac = tk.PhotoImage(file='imac.png')
        self.imag = tk.Label(self.hFrame,image=self.imac)
        self.imag.grid(row=1,column=0,ipadx=20,pady=20)
        self.imacinfo = tk.Text(self.hFrame,width=20,height=10)
        self.imscb = tk.Scrollbar(self.imacinfo)
        self.imscb.config(command=self.imacinfo.yview)
        self.imacinfo.config(yscrollcommand=self.imscb.set)
        self.imacinfo.grid(row=1,column=1)
        iminf= """ 3.2Ghz 8-core Intel Xeon W processor
Turbo Boost upto 4.2Ghz
32GB 2666Mhz ECC memory,configurable up to 128GB
1TB SSD storage
Radeon Pro Vega 56 qith 8GB HBM2 memory
10GB Ethernet
Four Thunderbolt 3 ports
27-inch Retina 5K 5120-by-2880 P3 display
        """
        self.imacinfo.insert('end',iminf)
        self.imacFrame = tk.Frame(self.hFrame)
        self.imacFrame.grid(row=1,column=2)
        self.impr = tk.Label(self.imacFrame,text="IMAC Price: Rs.50,000")
        self.impr.grid(row=0,column=0,ipadx=10,pady=5)
        self.imbtn = tk.Button(self.imacFrame,text="Buy Now",command=lambda : self.buy(1))
        self.imbtn.grid(row=1,column=0,ipadx=20,pady=25)
        
        #Product 2
        self.boat = tk.PhotoImage(file='boat.png')
        self.boatlbl = tk.Label(self.hFrame,image=self.boat)
        self.boatlbl.grid(row=1,column=3,ipadx=20,pady=20)
        self.boatinfo = tk.Text(self.hFrame,width=20,height=10)
        self.btscb = tk.Scrollbar(self.boatinfo)
        self.btscb.config(command=self.boatinfo.yview)
        self.boatinfo.config(yscrollcommand=self.btscb.set)
        self.boatinfo.grid(row=1,column=4)
        btinf= """Thumping Bass:boAt signature sonic high definition sound with super extra bass
boAt custom-designed 50mm driver,giving you the performance you could never have imagined
The softness of the faux leather on the ear pads makes boAt Rockersz 510 pleasurable to wear
"""
        self.boatinfo.insert('end',btinf)
        self.boatFrame = tk.Frame(self.hFrame)
        self.boatFrame.grid(row=1,column=5)
        self.btpr = tk.Label(self.boatFrame,text="boAt 510 Headphones Price: Rs.1,990")
        self.btpr.grid(row=0,column=0,ipadx=10,pady=5)
        self.btbtn = tk.Button(self.boatFrame,text="Buy Now",command=lambda : self.buy(2))
        self.btbtn.grid(row=1,column=0,ipadx=20,pady=25)
        
        #Product 3
        self.opt = tk.PhotoImage(file='oneplus6t.png')
        self.optg = tk.Label(self.hFrame,image=self.opt)
        self.optg.grid(row=2,column=0,ipadx=20,pady=20)
        self.optinfo = tk.Text(self.hFrame,width=20,height=10)
        self.optscb = tk.Scrollbar(self.optinfo)
        self.optscb.config(command=self.optinfo.yview)
        self.optinfo.config(yscrollcommand=self.optscb.set)
        self.optinfo.grid(row=2,column=1)
        optinf= """Camera:16+20MP Dual rear camera with Optical Image Stabilization,Super slow motion,Nightscape and Studio Lightning
Display:6,41-inch(16.2 cms) Full HD+ Optic AMOLED display with 2340 X 1080 pixels resolutions
Memory,Storage & SIM:6GB RAM | 128GB storage | Dual nano SIM (4G+4G)
Battery:3700mAh"""
        self.optinfo.insert('end',optinf)
        self.optFrame = tk.Frame(self.hFrame)
        self.optFrame.grid(row=2,column=2)
        self.optpr = tk.Label(self.optFrame,text="OnePlus 6t Price: Rs.39,900")
        self.optpr.grid(row=0,column=0,ipadx=10,pady=5)
        self.optbtn = tk.Button(self.optFrame,text="Buy Now",command=lambda : self.buy(3))
        self.optbtn.grid(row=1,column=0,ipadx=20,pady=25)
        
        #Product 4
        self.ps = tk.PhotoImage(file='ps4.png')
        self.psg = tk.Label(self.hFrame,image=self.ps)
        self.psg.grid(row=2,column=3,ipadx=20,pady=20)
        self.psinfo = tk.Text(self.hFrame,width=20,height=10)
        self.psscb = tk.Scrollbar(self.psinfo)
        self.psscb.config(command=self.psinfo.yview)
        self.psinfo.config(yscrollcommand=self.psscb.set)
        self.psinfo.grid(row=2,column=4)
        psinf= """4K Gaming
High dyanmic range with an HDR enabled TV
Enhanced games
1 year warranty
"""
        self.psinfo.insert('end',psinf)
        self.psFrame = tk.Frame(self.hFrame)
        self.psFrame.grid(row=2,column=5)
        self.pspr = tk.Label(self.psFrame,text="Play Station 4 Price: Rs.39,900")
        self.pspr.grid(row=0,column=0,ipadx=10,pady=5)
        self.psbtn = tk.Button(self.psFrame,text="Buy Now",command=lambda : self.buy(4))
        self.psbtn.grid(row=1,column=0,ipadx=20,pady=25)
        
    #Methods of Buttons
    def login(self,event=None):
        global loggedUser
        username = self.unt.get()
        password = self.pnt.get()
        try :
            db = sql.connect('localhost','root','','gadmart')
            c = db.cursor()
            sq = "select * from user where Username='{}'".format(username)
            c.execute(sq)
            data = c.fetchone()
            self.pas.set('')
            if data:
                if password == data[1]:
                    loggedUser=username
                    self.logFrame.grid_forget()
                    self.hFrame.grid()
                else:
                    messagebox.showerror("Error","Invalid Password,kindly check")
            else:
                messagebox.showerror("Error","Invalid Username,You Need to SignUp")
        except Exception as e:
            messagebox.showerror("Error","Database Connectivity Problem {}".format(e))
        
    def signup(self):
        self.sigFrame.grid()
        self.logFrame.grid_forget()
        
    def sign(self):
        user = self.uent.get()
        fname = self.fent.get()
        lname = self.lent.get()
        dob = self.dent.get()
        add = self.aent.get()
        pn = self.pent.get()
        pas = self.psent.get()
        rpas = self.rpsent.get()
        em = self.eent.get()
        if pas == rpas:
            try :
                db = sql.connect('localhost','root','','gadmart')
                c = db.cursor()
                sq2 = "select * from user where Username='{}'".format(user)
                c.execute(sq2)
                data = c.fetchone()
                if data:
                    messagebox.showinfo("INFO","Username Already Exist,Please Choose a Different One.")
                else:
                    sq1 = "insert into user values('{}','{}','{}','{}','{}','{}','{}');".format(user,pas,fname+lname,add,pn,dob,em)
                    if c.execute(sq1):
                        db.commit()
                        messagebox.showinfo("INFO","You have successfully Registered,Kindly Login")
                        self.sigFrame.grid_forget()
                        self.logFrame.grid()
                    else:
                        messagebox.showerror("Error","Data Cannot be Entered at the moment")
            except Exception as e:
                messagebox.showerror("Error","Database Connectivity Problem {}".format(e))
        else:
            messagebox.showinfo("INFO","Please Re-Enter Your Password,It did'nt matched")
            self.p.set('')
            self.rp.set('')
    def buy(self,button):
        global loggedUser,today
        prodid=''
        if button==1:
            prodid = 'Imac'
        elif button==2:
            prodid = 'boAtH'
        elif button==3:
            prodid = 'Opt6'
        elif button==4:
            prodid = 'Ps4'
        try :
            db = sql.connect('localhost','root','','gadmart')
            c=db.cursor()
            sqi = "Select * from prodinfo where ProdId='{}'".format(prodid)
            c.execute(sqi)
            pdata = c.fetchone()
            if pdata:
                qty = pdata[3]
                if qty > 0:
                    squ = "Select * from user where Username='{}'".format(loggedUser)
                    c.execute(squ)
                    udata = c.fetchone()
                    ueml = udata[6]
                    ppr = pdata[2]
                    sqinv = "insert into inventory values ('{}','{}','{}','{}','{}')".format(loggedUser,prodid,today,ppr,ueml)
                    squp = "Update prodinfo set Quantity = '{}' where ProdId='{}'".format(qty-1,prodid)
                    if c.execute(sqinv):
                        c.execute(squp)
                        db.commit()
                        m = messagebox.askquestion("ASK","Do you want us to Send you an Email of your Purchase")
                        if m =='yes':
                            server = sp.SMTP('smtp.gmail.com',587)
                            server.starttls()
                            useremail = 'youremailid@example.com'
                            userpassword = 'password'
                            server.login(useremail,userpassword)
                            message = """
                                    You Bought a Product from our
                                        GADGET MARKET
                                        Prod Id : '{}'
                                        Product Name : '{}'
                                        Price   : '{}'
                                        Your Address : '{}'
                                        """.format(prodid,pdata[1],ppr,udata[3])
                            server.sendmail(useremail,ueml,message)
                            server.quit()
                            messagebox.showinfo("MAIL CONFIRMATION","Your Mail has been Sent")
                    else:
                        messagebox.showerror("Error","There was Some Error while booking Product,Please Try in a While")
                else:
                    messagebox.showinfo("INFO","Sorry,This Product is Unavailable")
            else:
                messagebox.showinfo("INFO","Product Data can't be Extracted Try in a while")
        except Exception as e:
            messagebox.showerror("Error","Database Connectivity Error{}".format(e))
    def logout(self):
        global loggedUser
        self.hFrame.grid_forget()
        self.logFrame.grid()
        loggedUser =''
gdmart = Gadmart()
gdmart.master.title("Gadget Market")
gdmart.mainloop()