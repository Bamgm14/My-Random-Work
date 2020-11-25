def Cube(a):
    b={}
    for x in a:
        b[x]=x**3
    return b
a=[]
for x in range(int(input("Enter Limit:"))):
    a.append(int(input("Enter Number:")))
print (Cube(a))
