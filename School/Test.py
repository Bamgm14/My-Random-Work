import time as t
for k in range(2,1500):
    x=k**(1/(k-1))
    y=k**(k/(k-1))
    print (x,y,x**y,y**x)
    if x**y==y**x:
        t.sleep(2)
        print('True')
    else:
        t.sleep(2)
        print('False')
