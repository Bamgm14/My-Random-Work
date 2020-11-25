a=[]
b=""
while True:
    c=input("Enter Number(Enter String To Break):")
    if c.isalpha():
        break
    else:
        a.append(int(c))
d=a[0]
e=0
for x in range(1,len(a)):
    if a[x]<d:
        d=a[x]
        e=x
print ("\n","List\n",a,"\n","Min Number\n",d,"\n","Position\n",e)
