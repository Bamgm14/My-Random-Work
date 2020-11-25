a="#"
b="@"
c=1
d=int(input("Enter Number:"))
if d%2==0:
    f=d/2
else:
    f=d//2+1
h=f-3
e=1
g=2
while c<=d:
    if c<=2 or c==f:
        print (a*c)
        c+=1
    elif c>2 and c<f:
        print (a+(b*e)+a)
        c+=1
        e+=1
    elif c>f and c<d-1:
        print (a+(b*h)+a)
        c+=1
        h=h-1
    else:
        print (a*g)
        c+=1
        g=g-1
    
