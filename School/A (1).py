import random as r
import time
z="Number Inserted Out Of Range"
def z1():
    print ('Human is Batting')
    Run1=[]
    while True:
        g=int(input('Enter Number:')) 
        f=r.randrange(1,7)
        assert (g in range(1,7)),z
        if f==g:
            print ("Computer Number:",f)
            print ('Out') 
            break
        else:
            print ("Computer Number:",f)
            Run1.append(g)
def z2():
    print ('Comp is Batting') 
    Run2=[] 
    while True:
        g=int(input('Enter Number:')) 
        f=r.randrange(1,7)
        assert (g in range(1,7)),z
        if f==g:
            print ('Out') 
            break
        else:
            print ("Computer Number:",f)
            Run2.append(f)
    return sum(Run2)
def z3():
    a=r.randrange(1,7)
    b=int(input('Even Or Odd[0/1]:'))
    assert (b==0 or b==1),z
    c=int(input('Enter Number:')) 
    assert (c in range(1,7)) 
    if (a+c)%2==b:
        d=input('Batting Or Bowling[A/O]:')
    else:
        print ('Comp Choosing') 
        e=['A','O']
        d=r.choice(e)
    assert (d=='A' or d=='O'),"You didn't Choose 'O' or 'A'" 
    if d=='A':
        g=z1()
        f=z2()
    else:
        f=z2() 
        g=z1() 
    if g==f:
        print ('Draw')
        print ('Human:',g)
        print ('Comp:',f)
        User,h=input("Enter Name:")+" And Computer",g
    elif g>f:
        print ('You Win') 
        print ('Human:',g)
        print ('Comp:',f)
        User,h=input("Enter Name:"),g
    else:
        print ('Computer Wins') 
        print ('Human:',g)
        print ('Comp:',f)
        User,h="Computer",f
    assert User!="=","No '=' symbol"
    return User,h
def z4():
    try:
        User,h=z3()
        print (User+':',h)
        return User,h
    except AssertionError as e:
        print(e)
        print("RESTARTING",end='')
        for x in range(2):
            time.sleep(1)
            print(".",end='')
        time.sleep(1)
        print(".")
        z4()
User,h=z4()
def z5():
    z=open("ScoreBoard.txt","r+")
    y=z.read()
    w=''
    v=[]
    for x in y:
        if x=='\n':
            v.append(w)
            w=''
        else:
            w+=x
    z.close()
    u=str(len(v)+1)+'.'+User+'='+str(h)
    v.append(u)
    z=open("ScoreBoard.txt","w+")
    for x in range(len(v)):
        z.write(v[x]+'\n')
    z.close()
def z6():
    z=open("ScoreBoard.txt","r+")
    a=z.read()
    z.close()
    b=''
    c=[]
    for x in a:
        if x=='\n':
            c.append(b)
            b=''
        else:
            b+=x
    d=[]
    g=[]
    for x in c:
        f=0
        for y in x:
            if y=='=':
                f=1
                continue
            if f==1:
                b+=y
        d.append(int(b))
        g.append(int(b))
        b=''
    e=[]
    while len(d)>0:
        e.append(max(d))
        d.remove(max(d))
    h=[]
    for x in e:
        a=g.index(x)
        h.append(c[a])
    z=open("LeaderBoard.txt","w+")
    for x in range(len(h)):
        z.write(str(x+1)+'.'+h[x]+"\n")
    z.close()
try:
    z5()
    z6()
except FileNotFoundError:
    z=open("ScoreBoard.txt","w+")
    z.close()
    z5()
