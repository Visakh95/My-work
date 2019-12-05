'''
Created on Apr 30, 2019

@author: mice
'''
from tkinter import messagebox
from tkinter import *
'''
root=Tk()
w=Label(root,text='Hello,world!')
w.pack()
root.mainloop()
'''

class App:
    def __init__(self,master):
        frame=Frame(master)
        frame.pack()
        self.button=Button(frame,text="QUIT",bg="lightblue",fg="red",command=frame.quit)
        self.button.grid(row=0,column=1)
        self.hi_there=Button(frame,text="Hello",bg="yellow",fg="red",command=self.say_hi)
        self.hi_there.grid(row=0,column=10)
    def say_hi(self):
        print("hi there,everyone!")
def callback():
    if messagebox.askokcancel("Quit","Do you really wish to quit?"):
        root.destroy()
root=Tk()
app=App(root)
root.mainloop()

'''
root=Tk()
def callback(event):
    print("clicked at",event.x,event.y) 
frame=Frame(root,width=100,height=100)
frame.bind("<Button-1>",callback)
frame.pack()
root.mainloop()       
'''