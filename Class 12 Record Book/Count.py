def Count(file='Weird.txt'):
    f=open(file,'r').readlines()
    lst=[]
    done={}
    for x in f:
        lst+=x.split(' ')
    for x in lst:
        if x not in done.keys():
            done[x]=lst.count(x)
    return done
print(Count())
