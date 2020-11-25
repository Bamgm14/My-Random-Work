def Length(file='Weird.txt'):
    return len(list(open(file,'r').readlines()))
print(Length())
