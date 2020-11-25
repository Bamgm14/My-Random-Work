a=" "
b="* "
c=1
d=int(input("Enter Number:"))
f=0
if d%2==0:
    e=d/2
else:
    e=(d//2)+1
while c<=d:
    if c<=2:
        print (a*(d-c),b*c)
        c+=1
    elif c>=d-1:
        print (a*(c-1),b*((d-(c-1)))) 
        c+=1
    elif c>2 and c<e:
        print (a*(d-c),b,a*f,b)
        c+=1
        f+=2
    else:
        print (a*(c-1),b,a*f,b)
        f-=2
        c+=1
