a=int(input("Enter Number:"))
b=str(a)
c=len(b)
d=1
e=[]
f=10
g=0
h=1
while d<=c:
    g=a%10
    e.append(g)
    a=a//10
    d+=1
for x in e:
    print (x*(f**c))
    h+=1
