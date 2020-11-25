import time
def encrypt(a):
    b=[]
    for x in range(len(a)):
        b.append(ord(a[x])^x)
    return b
a=input('Enter String:')
b=encrypt(a)
for x in b:
    x=hex(x)
    x=x[2:]
    print('\\x'+x,end='')
time.sleep(10)
