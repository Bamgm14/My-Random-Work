a=" "
b="* "
c=1
d=int(input("Enter Number:"))
if d%2==0:
    e=d/2
else:
    e=(d//2)+1
while c<=d:
    if c<=e:
        print (b*c)
        c+=1
    else:
        print (b*(d-(c-1)))
        c+=1
