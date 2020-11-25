def m(a):
    f=1
    b=0
    for x in range(a):
        b=b+f
        f+=2
    return b
a=int(input("enter a number"))
print("sum of first n odd numbers is",m(a))
