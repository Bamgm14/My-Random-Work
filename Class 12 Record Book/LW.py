def ListWord(n,file='Weird.txt'):
    return list(open(file,'r').readlines())[0:n]
print(ListWord(1))
