import os
from tkinter import *
def snl():
    def pla():
        if str(pm.get())!='':
            a=int(str(pm.get()))
            print (a)
            try:
                a=int(str(pm.get()))
                snl1(a)
            except:
                txt.configure(text='Invalid Input')
    global root
    global sl
    global a
    root.destroy()
    sl=Tk()
    sl.title('Snakes And Ladders')
    sl.geometry('350x250')
    Pl=Label(sl,text='Number Of Players',font=(10)).pack()
    txt=Label(sl,text='')
    txt.pack()
    pm=Entry(sl)
    pm.pack()
    pl=Button(sl, text='Enter', command= pla).pack()
    sl.mainloop()
def snl1(a):
    global sl
    b=open('Player.py','w+')
    b.write("""import random as r
import os
a=open('SnL.py','w+')
a.write('''import random as r
import time as t
def a(n,q):
    global Ladders
    global Snakes
    a=r.randrange(1,7)
    print ("Player "+str(q)+" Moved "+str(a))
    n.append(a)
    b=r.randrange(1,11)
    if sum(n) in Snakes:
        print ("Oh No... The Snake Got You... Move "+str(b)+" Backward!!")
        n.append(-b)
    b=r.randrange(1,11)
    if sum(n) in Ladders:
        print ("Yay... You Found A Ladder... Move "+str(b)+" Forward!!")
        n.append(b)
    print ("Current Position:"+str(sum(n)))\\n''')
b=[]
for x in range("""+str(a)+"""):

    c=input('Enter Name:')
    c.replace(' ','_')
    b.append(c)
d=int(input('Enter Difficulty[1,2,3,4]:'))
assert d in [1,2,3,4]
Snakes=[]
Ladders=[]
while len(Snakes)!=(d*5) or len(Ladders)!=(d*5):
    e=r.randrange(1,100)
    if (e not in Snakes) and (len(Snakes)!=(d*5)):
        Snakes.append(e)
    if (e not in Snakes) or (e not in Ladders) and (len(Ladders)==(d*5)):
        Ladders.append(e)
a.write('Snakes='+str(Snakes)+'\\nLadders='+str(Ladders)+'\\n')
for x in b:
    a.write('\\n'+x+'=[]')
a.write('\\nwhile True:\\n')
for x in range(len(b)):
    a.write('\\ta('+b[x]+','+str(x+1)+')\\n')
    a.write('\\tif sum('+b[x]+')>=100:\\n')
    a.write('\\t\\tprint("'+b[x]+' Is Winner")\\n')
    a.write('\\t\\tt.sleep(5)\\n')
    a.write('\\t\tbreak\\n')
    a.write('\\tt.sleep(1)\\n')
a.close()
os.system('attrib +h SnL.py & python3 SnL.py')
""")
    b.close()
    sl.destroy()
    os.system('attrib +h Player.py & python3 Player.py')
    exit()
def rot():
    root=Tk()
    root.title('Game Chooser')
    root.geometry('350x250')
    Title=Message(root,text='Games',font=("Times", 15, "bold")).pack()
    SnL=Checkbutton(root,text='Snakes And Ladders',command=snl).pack()
    O_E=Checkbutton(root,text='Odd Or Even').pack()
    Bull=Checkbutton(root,text='Bull').pack()
    root.mainloop()
try:
    pokemon=os.getcwd()
    os.system('cd '+str(pokemon)+'& del /f Player.py & del /f SnL.py')
    rot()
except:
    print ('Error')
