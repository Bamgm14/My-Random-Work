import time
a=open("1.txt","r+",errors='ignore')
b=a.read()
c=''
for x in b:
    if x=='\n':
        print(c)
        time.sleep(.5)
        c=''
    else:
        c+=x
if 'color' in c:
    print ("Yes")
a.close()
