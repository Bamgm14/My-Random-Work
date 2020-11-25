import random as r
a=open('SnL.py','w+')
a.write('''import random as r
import time as t
def a(n,q):
    global Ladders
    global Snakes
    a=r.randrange(1,7)
    print ("Player "+str(q)+" Moved "+str(a))
    n.append(a)
    b=r.randrange(1,11)
    if sum(n) in Snakes:
        print ("Oh No... The Snake Got You... Move "+str(b)+" Backward!!")
        n.append(-b)
    b=r.randrange(1,11)
    if sum(n) in Ladders:
        print ("Yay... You Found A Ladder... Move "+str(b)+" Forward!!")
        n.append(b)
    print ("Current Position:"+str(sum(n)))\n''')
b=[]
for x in range(int(input('Enter Number Of Players:'))):
    c=input('Enter Name:')
    c.replace(' ','_')
    b.append(c)
d=int(input('Enter Difficulty[1,2,3,4]:'))
assert d in [1,2,3,4]
Snakes=[]
Ladders=[]
while len(Snakes)!=(d*5) or len(Ladders)!=(d*5):
    e=r.randrange(1,100)
    if (e not in Snakes) and (len(Snakes)!=(d*5)):
        Snakes.append(e)
    if (e not in Snakes) or (e not in Ladders) and (len(Ladders)==(d*5)):
        Ladders.append(e)
a.write('Snakes='+str(Snakes)+'\nLadders='+str(Ladders)+'\n')

for x in b:
    a.write('\n'+x+'=[]')
a.write('\nwhile True:\n')
for x in range(len(b)):
    a.write('\ta('+b[x]+','+str(x+1)+')\n')
    a.write('\tif sum('+b[x]+')>=100:\n')
    a.write('\t\tprint("'+b[x]+' Is Winner")\n')
    a.write('\t\tt.sleep(5)\n')
    a.write('\t\tbreak\n')
    a.write('\tt.sleep(1)\n')
a.close()
