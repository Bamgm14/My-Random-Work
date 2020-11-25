import time
def encrypt_1(a):
    b=[]
    c=[]
    for x in range(len(a)):
        if x>=len(a)//2:
            c.append(a[x])
            continue
        else:
            b.append(a[x])
            continue
    d=(''.join(c))+(''.join(b))
    return d
def encrypt_2(a):
    b=[10,20,15]
    c=[]
    import random as r
    for x in a:
        c.append(ord(x)-r.choice(b))
    return c
a=input("Enter String:")
b=(encrypt_2(encrypt_1(a)))
for x in b:
    x=hex(x)
    x=x[2:]
    print('\\x'+x,end='')
time.sleep(10)
