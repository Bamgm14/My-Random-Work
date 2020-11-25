from tkinter import *
import os
def z(a):
    global f
    f=str((d.get(d.curselection())))
    y(f)
def y(a):
    global e
    global f
    global j
    j=Tk()
    j.title(a)
    r=Label(j,text='').grid(row=0,column=1)
    l=Label(j,text='Number 1').grid(row=1)
    k=Entry(j).grid(row=2)
    m=Label(j,text='Number 2').grid(row=3)
    n=Entry(j).grid(row=4)
    q=Button(j,text="Answer").grid(row=5)
    q.bind('<Return>',v)
    j.mainloop()
def v():
    if e[0]==f:
        r=Label(j,text=str(int(k.get())+int(n.get()))).grid(row=0,column=1)
    #if e[1]==f:
    #    r=Label(j,text=str(int(k)-int(n))).grid(row=0,column=1)
    #if e[2]==f:
    #    r=Label(j,text=str(int(k)*int(n))).grid(row=0,column=1)
    #if e[3]==f:
    #    r=Label(j,text=str(int(k)/int(n))).grid(row=0,column=1)
e=["Add","Subtract","Multiple","Divide"]
a=Tk()
a.title("Python GUI")
b=Label(a,text='This Is My First GUI Program',anchor=N,font=("Arial", 16))
b.grid(row=0)
c=Label(a,text="So What Would You Like To Do?",font=("Arial"))
c.grid(row=1)
d=Listbox(a)
f=''
k=0
n=0
for x in range(len(e)):
    d.insert(END,e[x])
d.bind('<<ListboxSelect>>',z)
d.grid(row=2)
a.mainloop()
