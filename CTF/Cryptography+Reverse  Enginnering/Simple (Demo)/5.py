import time
def encrypt(a,n,nc):
    b=[]
    for x in range(1,nc+1):
        b.append(ord(a[x-1])^n)
    return b
def keycreate(n):
    import random as r
    n=r.randrange(n)
    n=(n+46638)%10
    return n
a=input("Enter String:")
b=encrypt(a,keycreate(len(a)),len(a))
for x in b:
    x=hex(x)
    x=x[2:]
    print('\\x'+x,end='')
time.sleep(10)
