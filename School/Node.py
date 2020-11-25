import sys
NodeMap={"A":[("B",7),("C",2),("M",3)],
         "B":[("A",7),("C",3),("D",4)],
         "C":[("A",2),("B",3),("D",4),("E",1)],
         "D":[("B",4),("C",4),("F",5)],
         "E":[("C",1),("F",3),("G",2)],
         "F":[("D",5),("E",3)],
         "G":[("E",2),("H",2)],
         "H":[("G",2),("I",5)],
         "I":[("H",5),("J",4),("K",4)],
         "J":[("I",4),("K",6),("L",4)],
         "K":[("I",4),("J",6),("L",4)],
         "L":[("K",4),("J",4),("M",2)],
         "M":[("A",3),("L",2)]}
Start="A"
End="I"
flag=False
Stack={}
for x in NodeMap.keys():
    if Start==x:
        Stack[x]=(None,0)
    else:
        Stack[x]=(None,sys.maxsize)
lst=[(None,Start)]
flag=False
for x in lst:
    posi=x[1]
    for y in NodeMap[posi]:
        dis=y[1]+Stack[posi][1]
        if End==posi:
            flag=True
            break
        if y[0] not in [z[1] for z in lst] and Stack[y[0]][1]>dis:
            Stack[y[0]]=(posi,dis)
    del Stack[posi]
    if flag:
        lst+=[(posi,None)]
        break
    else:
        srt=sorted([(y,Stack[y]) for y in Stack.keys()],key=lambda y:y[1][1])[0]
        lst+=[(srt[1][0],srt[0])]
lst.reverse()
lst1=[]
for x in lst:
    if x[1]==End:
        lst1.append(x[1])
        End=x[0]
print(lst1)
