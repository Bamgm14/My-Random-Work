a=[]
while True:
    b=input('Enter Number(Use String To Break):')
    if b.isalpha():
        break
    else:
        a.append(int(b))
while len(a)>0:
    b=a[0]
    c=0
    while b in a:
        a.remove(b)
        c+=1
    
    print ("Number:",b,"\nFreq:",c)
