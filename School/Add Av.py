a=[]
b=''
c=0
while True:
    b=input('Enter Number(Use String To Break):')
    if b.isalpha():
        break
    else:
        a.append(int(b))
for x in a:
    c+=x
d=len(a)
print (c/d)
