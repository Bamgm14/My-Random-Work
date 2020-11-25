import random as r
def Fortune(file='Weird.txt'):
    f=open(file,'r').readlines()
    print(f[r.randint(0,len(f))-1])
Fortune()
