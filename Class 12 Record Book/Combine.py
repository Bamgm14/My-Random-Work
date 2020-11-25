def Suggestive(file1='Weird.txt',file2='Weirdv2.txt'):
    lst1=open(file2,'r').readlines()
    lst2=open(file1,'r').readlines()
    if len(lst1)>=len(lst2):
        Len=(len(lst1),lst1)
    else:
        Len=(len(lst2),lst2)
    for x in range(Len[0]):
        try:
            print(lst1[x]+lst2[x])
        except:
            print(Len[1][x])
Suggestive()
