def Copy(file1='Weird.txt',file2='Weirdv2.txt'):
    f=open(file2,'w')
    lst=open(file1,'r').readlines()
    for x in lst:
        f.write(x)
    f.close()
Copy(file1='Weird.txt',file2='Weirdv2.txt')
