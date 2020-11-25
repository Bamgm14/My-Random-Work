import random as r
import time
Run1=[]
Run2=[]
z="Number Inserted Out Of Range"
def z1(x):
    print ('Human is Batting')
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
            x.append(g)
    return sum(x)
def z2(x):
    print ('Comp is Batting')  
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
            x.append(f)
    return sum(x)
def z8():
    a=input("Do you want restart the Game?[Y/N]:")
    assert a=='Y' or a=='N' or a=='y' or a=='n',"Please Enter 'Y' or 'N'"
    if a=='Y' or a=='y':
        b=0
    else:
        b=1
    return b
def z9():
    try:
        a=z8()
    except AssertionError as e:
        print (e)
        for x in range(3):
            print ("-",end='')
            time.sleep(0.5)
        print ("-")
        a=z9()
    return a
def z7():
    global Run1
    global Run2
    try:
        m=z1(Run1)
    except AssertionError as e:
        print (e)
        a=z9()
        if a==1:
            m=z1(Run1)
        else:
            Run2=[]
            Run1=[]
            print("RESTARTING",end='')
            for x in range(2):
                time.sleep(1)
                print(".",end='')
            time.sleep(1)
            print(".")
    except ValueError as e:
        print (e)
        a=z9()
        if a==1:
            m=z1(Run1)
        else:
            Run2=[]
            Run1=[]
            print("RESTARTING",end='')
            for x in range(2):
                time.sleep(1)
                print(".",end='')
            time.sleep(1)
            print(".")
    return m
def z10():
    global Run1
    global Run2
    try:
        m=z2(Run2)
    except AssertionError as e:
        print (e)
        a=z9()
        if a==1:
            m=z2(Run2)
        else:
            Run2=[]
            Run1=[]
            print("RESTARTING",end='')
            for x in range(2):
                    time.sleep(1)
                    print(".",end='')
            time.sleep(1)
            print(".")
    except ValueError as e:
        print (e)
        a=z9()
        if a==1:
            m=z2(Run2)
        else:
            Run2=[]
            Run1=[]
            print("RESTARTING",end='')
            for x in range(2):
                time.sleep(1)
                print(".",end='')
            time.sleep(1)
            print(".")
    return m
'''
def z3():
    a=r.randrange(1,7)
    b=int(input('Even Or Odd[0/1]:'))
    assert (b==0 or b==1),z
    c=int(input('Enter Number:')) 
    assert (c in range(1,7)),z
    return a,b,c
def z13(a,b,c):
    if (a+c)%2==b:
        d=input('Batting Or Bowling[A/O]:')
    else:
        print ('Comp Choosing') 
        e=['A','O']
        d=r.choice(e)
    assert (d=='A' or d=='O' or d=='a' or d=='o'),"You didn't Choose 'O' or 'A'"
    return d
'''
def z11(d):
    if d=='A' or d=='a':
        g=z7()
        f=z10()
    else:
        f=z10() 
        g=z7() 
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
    assert User!="=" or User!='.',"No '=' or '.' symbol"
    return User,h
def z12():
    try:
        am,bm,cm=z3()
    except AssertionError as e:
        print(e)
        print("RESTARTING",end='')
        for x in range(2):
            time.sleep(1)
            print(".",end='')
        time.sleep(1)
        print(".")
        am,bm,cm=z12()
    return am,bm,cm
'''
def z14(a,b,c):
    try:
        f=z13(a,b,c)
    except AssertionError as e:
        print(e)
        print("RESTARTING",end='')
        for x in range(2):
            time.sleep(1)
            print(".",end='')
        time.sleep(1)
        print(".")
        f=z14(a,b,c)
    return f
'''
def z4(d):
    try:
        User,h=z11(d)
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
        z4(d)
def z15():
    x,v,n=z12()
    d=z14(x,v,n)
    User,h=z4(d)
    try:
        z5(User,h)
        z6()
    except FileNotFoundError:
        z=open("ScoreBoard.txt","w+")
        z.close()
        z5(User,h) 
def z5(User,h):
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
        g[a]=-1
    z=open("LeaderBoard.txt","w+")
    for x in range(len(h)):
        z.write(str(x+1)+'.'+h[x]+"\n")
    z.close()
def z17():
    a=input("Do you want to play again[Y/N]:")
    assert a=="Y" or a=="y" or a=="N" or a=="n","Please Enter 'Y' or 'N'"
    if a=="Y" or a=="y":
        z15()
    else:
        exit()
def z18():
    try:
        Run1=[]
        Run2=[]
        z17()
        z18()
    except AssertionError as e:
        print (e)
        z18()
z15()
z18()
