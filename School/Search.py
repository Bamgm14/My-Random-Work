a=[]
b=''
c=0
while True:
    b=input('Enter Number(Use String To Break):')
    if b.isalpha():
        break
    else:
        a.append(int(b))
d=int(input("Search Number:"))
if d in a:
    print ("Yes")
else:
    print ("No")
