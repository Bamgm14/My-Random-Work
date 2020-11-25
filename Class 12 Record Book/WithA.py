def RemoveA(file1='Weird.txt',file2='WeirdButA.txt'):
    f=open(file2,'a')
    lst=open(file1,'r').readlines()
    f1=open(file1,'w')
    for x in lst:
        if 'a' in x or 'A' in x:
            f.write(x)
        else:
            f1.write(x)
    f.close()
    f1.close()
    print(open(file1,'r').read(),open(file2,'r').read())
RemoveA()
