a=[]
while True:
    b=input('Enter Number(Use String To Break):')
    if b.isalpha():
        break
    else:
        a.append(int(b))
c=[]
while len(a)>0:
    b=a[0]
    for x in a:
        if x>b:
            continue
        else:
            b=x
    a.remove(b)
    c.append(b)
print (c)
