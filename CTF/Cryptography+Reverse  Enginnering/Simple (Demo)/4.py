import time
a=input("Enter String:")
b=(len(a)%6)**(len(a)%3)
for x in a:
    x=hex(ord(x)^b)
    x=x[2:]
    print('\\x'+x,end='')
time.sleep(10)
