def ReadWrite(Write='NSA',file='Weird.txt'):
    f=open(file,'a')
    f.write(Write+'\n')
    f.close()
    for x in open(file,'r').readlines():
        print(x)
ReadWrite()
