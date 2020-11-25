import tkinter as tk
from tkinter import *
def evl():
    command=eval(entry.get())
    print(str(command))
    label2.config(text=str(command))
root = Tk()
root.title=("Python/Calculator Evalulator")
root.geometry('350x350')
root.configure(background="wheat1")
label1=Label(root,text="Enter Below:",fg="black")
entry=Entry(root)
label1.pack()
entry.pack()
button=Button(root,text="Eval",command=evl)
button.pack()
label2=Label(root,text="",fg="black")
label2.pack()
root.mainloop()

