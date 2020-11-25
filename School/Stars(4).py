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
        print (b*c)
        c+=1
    elif c>=d-1:
        print (b*(d-(c-1))) 
        c+=1
    elif c>2 and c<e:
        print (b,a*f,b)
        c+=1
        f+=2
    else:
        print (b,a*f,b)
        c+=1
        f-=2
