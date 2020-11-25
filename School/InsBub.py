def Bubble(a):
    for x in range(len(a)-1,0,-1):
        for i in range(x):
            if a[i]>a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
def Insert(a):
    for x in range(1,len(a)):
        currentvalue = a[x]
        position = x
        while position>0 and a[position-1]>currentvalue:
            a[position]=a[position-1]
            position = position-1
            a[position]=currentvalue
import random as r
b=[]
c=[]
d=[]
for x in range(100000):
    v=r.randrange(-999,1000)
    b.append(v)
    c.append(v)
    d.append(v)
print (b)
import time as t
a=t.time()
Bubble(b)
print (b,t.time()-a)
a=t.time()
Insert(c)
print (c,t.time()-a)
a=t.time()
d.sort()
print (d,t.time()-a)
if c==d:
    print ('Yes C')
if b==d:
    print ('Yes B')
