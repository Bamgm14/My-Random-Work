import time
def encrypt(a):
    import random as r
    b=[]
    for x in range(len(a)):
        b.append(ord(a[x])^(r.randrange(1,11)))
    return b
a=input("Enter Strings:")
b=encrypt(a)
for x in b:
    x=hex(x)
    x=x[2:]
    print('\\x'+x,end='')
time.sleep(10)
