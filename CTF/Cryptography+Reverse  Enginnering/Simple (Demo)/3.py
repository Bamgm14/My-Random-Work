import time
a=input("Enter String:")
b=[]
c=[]
x=0
if len(a)%2!=0:
    a+='\n'
while x<len(a):
    b.append(ord(a[x])^x)
    b.append(ord(a[x+1])^x)
    x+=2
for x in b:
    x=hex(x)
    x=x[2:]
    print('\\x'+x,end='')
time.sleep(10)
