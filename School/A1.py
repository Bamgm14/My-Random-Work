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
z6()
