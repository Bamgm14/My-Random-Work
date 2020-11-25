a=[]
e=a
b=''
while True:
    b=input('Enter Number(Use String To Break):')
    if b.isalpha():
        break
    else:
        a.append(int(b))
while len(a)>0:
    c=a[0]
    for x in a:
        d=0
        if c==x:
            d+=1
            a.remove(x)
        else:
            continue
        print ("Number:",c)
        print ("Frequency:",d)
