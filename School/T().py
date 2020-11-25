from tkinter import *
ls=[]
def e():
    if d.get()!='':
        ls.append(str(d.get()))
        a.destroy()
    else:
        b.configure('Player User Missing')
a=Tk()
a.title('Snakes And Ladders')
b=Label(a,text='Usernames',font=((10))).grid(row=0)
txt=Label(a,text='')
txt.grid(row=1)
c=Label(a,text='Player 1')
c.grid(row=2,column=0)
d=Entry(a)
d.grid(row=2,column=1)
f=Button(a,text='Construct',command=e).grid(row=2)
a.mainloop()
print(ls)
