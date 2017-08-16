from tkinter import *
from tkinter import messagebox
top = Tk()

# method to define the action when a button is clicked
#Bit Map represents the icons which can be used instead of text. 
def callbackfunc():
    msg = Tk()
    text = Text(msg)
    text.insert(INSERT,"Hello")
    text.place(x = 10,y = 10) 

    #canvas 

def drawcnvas():
    topCanavs = Tk()
    C = Canvas(topCanavs,bg = "blue", height = 250, width = 300)
    coord = 10, 50, 240, 210
    arc = C.create_arc(coord,start=0,extent=150,fill="red")
    line = C.create_line(10,10,100,100)
    C.pack()  

# checkbox

def chkBtn():
    topChkBtn = Tk()
    Chk1 = Checkbutton(topChkBtn,text="Music",onvalue = 1, offvalue = 0, height=5,width = 20)      
    Chk2 = Checkbutton(topChkBtn,text="Video",onvalue = 1, offvalue = 0, height=5,width = 20)
    Chk1.pack()
    Chk2.pack()

# Entry (textBox) , Label   

def entry():
    ex = Tk()
    L1 = Label(ex,text="User Name")
    L1.grid(row=0,column=0)
    E1 = Entry(ex,bd=5)
    E1.grid(row=0,column=1)
    L2 = Label(ex,text="Password",)
    L2.grid(row=1,column=0)
    E2 = Entry(ex,bd=5,show=".")
    E2.grid(row=1,column=1)
    

# Frames

def frames():
    frm = Tk()
    frame1 = Frame(frm,bd=5,bg="Gray")
    L1 = Label(frame1,text="User Name")
    L1.grid(row=0,column=0)
    E1 = Entry(frame1,bd=5)
    E1.grid(row=0,column=1)
    L2 = Label(frame1,text="Password",)
    L2.grid(row=1,column=0)
    E2 = Entry(frame1,bd=5,show=".")
    E2.grid(row=1,column=1)
    frame1.pack()
    frm.mainloop()

# ListBox

def lstbox():
    lstbox = Tk()
    data = [1,2,3,4,5,6,7,8,9]
    LB1 = Listbox(lstbox)
    for item in data:
        LB1.insert(END,item)
    LB1.pack()
    lstbox.pack()    
    lstbox.mainloop()   

# MenuButton and Menu

def menusummary():
    menusummary = Tk()
    #Menu button
    mb = Menubutton(menusummary,text="MenosGorrande", relief = RAISED)
    mb.grid()
    #Menu
    menu = Menu(mb,tearoff=0)
    mb["menu"] = menu
    #mayoVar  = IntVar()
   # mb.menu.add_checkbutton ( label = "mayo", variable = mayoVar )
    menu.add_command(label="Espada")
    menu.add_command(label="Arroncar")
    menu.add_command(label="Ryoka")
    menu.add_command(label="Hallow")
    menu.add_command(label="S.reaper")
    menu.add_separator()
    menu.add_command(label="Squad 0")
    menu.add_command(label="Reattsu")
    mb.pack()
    menusummary.mainloop()     

# Message

def msg():
    msg = Tk()
    whatever_you_do = "Hello!\nMessage is transmitted.\nMessage Acknowledged."
    msg1 = Message(msg, text = whatever_you_do)
    msg1.config(bg='gray', font=('times', 20, 'italic'))
    msg1.pack()
    msg.mainloop()   
# Radio button and scale(slider) and SpinBox

def rdbtn():
    def sel():
        var = inco.get()
        selection = "You selected the option" + str(var)    
        label.config(text=selection)
    rdbtn = Tk()
    inco = IntVar()
    btn1 = Radiobutton(rdbtn,text='Option1',variable = inco,value = 1,command=sel)
    btn1.pack()
    btn2 = Radiobutton(rdbtn,text='Option2',variable = inco,value = 2,command=sel)
    btn2.pack()
    btn3 = Radiobutton(rdbtn,text='Option3',variable = inco,value = 3,command=sel)
    btn3.pack()
    scale = Scale( rdbtn, variable = inco )
    scale.pack(anchor = CENTER)
    label = Label(rdbtn)
    label.pack()
    w = Spinbox(rdbtn,from_ = 10,to = 30)
    w.pack()
    rdbtn.mainloop()    
#Paned Window

def pw():
    pw = Tk()
    m1 = PanedWindow()
    m1.pack(fill = BOTH, expand = 1)
    left = Entry(m1,bd=5)
    m1.add(left)
    pw.mainloop()

# LabelFrame

def lf():
    lf = Tk()
    labelframe = LabelFrame(lf, text = "This is a LabelFrame")
    labelframe.pack(fill = "both", expand = "yes")
    left = Entry(labelframe,bd=5)
    left.pack()
    lf.mainloop()

# Message Box

def hello():
    messagebox.showinfo("Say Hello", "Hello World")
    messagebox.showwarning("Say Hello", "Hello World")
    messagebox.showerror ("Say Hello", "Hello World")
    messagebox.askquestion("Say Hello", "Hello World")
    messagebox.askokcancel("Say Hello", "Hello World")
    messagebox.askyesno ("Say Hello", "Hello World")
    messagebox.askretrycancel ("Say Hello", "Hello World")

#button

B= Button(top,text="Hello",bg="black",fg="red",width=20,command=hello)
B.place(x = 10,y = 100)


top.mainloop()

