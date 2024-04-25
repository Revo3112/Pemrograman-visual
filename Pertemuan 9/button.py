from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("100x100")
def Hallo():
   msg=messagebox.showinfo( "Hello Python", "Hello Revo")
B = Button(top, text ="Hello", command = Hallo)
B.place(x=50,y=50)
top.mainloop()
