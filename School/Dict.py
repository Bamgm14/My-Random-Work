def Dict(a):
    b={}
    for x in a:
        b[x]=len(x)
    return b
a=[]
for x in range(int(input("Enter Limit:"))):
    a.append(input("Enter String:"))
print (Dict(a))
