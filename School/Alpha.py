a="A"
b=ord(a)
c=1
d=int(input("Enter Number:"))
e=0
f=0
while c<=d:
    if c<d:
        print (a+((" ")*((2*e)-2)),a*f)
        e+=1
        if f==0:
            f=1
        c+=1
        b+=1
        a=chr(b)
    else:
        g=a+" "
        print (g*c)
        c+=1
