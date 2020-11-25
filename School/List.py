a=[]
for x in range(1,100001):
    b=input("Enter Name(Type .exit When Finished Entering):")
    if b==".exit":
        break
    a.append(b)
print (a)
c=input("Enter Name To Be Removed:")
for y in a:
    if a==c:
        a.remove(c)
    else:
        continue
print (a)
