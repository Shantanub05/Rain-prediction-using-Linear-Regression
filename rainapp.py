
from logging import root
from this import d
from tkinter import *
from tkinter import messagebox

top=Tk()
top.geometry("1920x1080")
top.attributes('-fullscreen', True)
c=Canvas(top,bg="gray16",height=200,width=200)
c.pack()
filename=PhotoImage(file="D:/SEM 4/ITME/zx.png")
background_label=Label(top,image=filename)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
def ins():
    root=Toplevel()
    
    root.geometry("1920x1080")
    root.attributes('-fullscreen', True)
    d=Canvas(top,bg="gray16",height=200,width=200)
    d.pack()
    filename=PhotoImage(file="D:/SEM 4/ITME/mx.png")
    background_label=Label(root,image=filename)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    mytext = self.canvas.create_text(100,10,fill="darkblue",font="Times 20 italic bold",text="Click the bubbles that are multiples of two.")
    E1 = Entry(root, bd = 10)
    E1.place(x = 260,y = 300)
    d.create_text(220,340,text="Branch")
    E2 = Entry(root,bd = 10)
    E2.place(x = 260,y = 370)
    E3 = Entry(root, bd = 10)
    E3.place(x = 260,y = 440)
    E4 = Entry(root, bd = 10)
    E4.place(x = 260,y = 510)
    E5 = Entry(root, bd = 10)
    E5.place(x = 260,y = 580)
    E6 = Entry(root, bd = 10)
    E6.place(x = 260,y = 650)
    root.mainloop()
    top.destroy()
A = Button(top, text = "Predict",command=ins)
A.place(x = 300, y = 360)

top.mainloop()

