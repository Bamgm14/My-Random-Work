import os
a=[]
for x in os.listdir(r'C:\Users\Bamgm14\Desktop\Meme'):
    a.append(str(x))
for x in a:
    print (x,end=' ')
#for x in range(len(a)):
#    os.rename(a[x],'b('+str(x)+')'+a[x][-6:])
