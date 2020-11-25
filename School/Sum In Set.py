a=[]
c=0
d=0
while True:
    b=input("Enter NumberList (1)[When Finished Type Exit]:")
    if b=="exit" or b=="Exit":
        break
    elif b.isalpha():
        pass
    else:
        a.append(int(b))
for x in a:
    d+=x
print (d)
