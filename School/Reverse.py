a=[]
while True:
    b=input('Enter Number(Use String To Break):')
    if b.isalpha():
        break
    else:
        a.append(int(b))
b=len(a)-1
c=[]
while b>=0:
    d=a[b]
    c.append(d)
    b-=1
print (c)
