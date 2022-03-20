#import the needed libraries (Note : tkinter library is used to produce GUI)
from tkinter import *
from tkinter.ttk import *
from time import strftime

#give title

root = Tk()
root.title("Clock")

#define the format of the time you need

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)

#define the design you need in your clock
label = Label(root, font=("ds-digital",80),background = "black", foreground ="cyan")

#to define the position of the projection on the application 

label.pack(anchor='center')


time()

#to run the tkinter event loop

mainloop()