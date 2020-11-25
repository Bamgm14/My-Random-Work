a=[]
while True:
    b=input("Enter Number(Break Using String):")
    if b.isalpha():
        break
    else:
        a.append(int(b))
        continue
c=a[0]
for x in a:
    if c>x:
        c=x
    else:
        continue
d=0
if c in a:
    d=a.index(c)
print ("Index:",d)
print ("Number:",c)
