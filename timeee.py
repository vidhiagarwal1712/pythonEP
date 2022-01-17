from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def getTime():      
    t=strftime('%H %M %S : %p')
    label.config(text=t)
    label.after(1000,getTime)   


label= Label(root,font=('ds-digital',80),background="black",foreground="cyan")
label.pack(anchor='center')

getTime()

mainloop()