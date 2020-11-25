import os
def SizeAndBig(file='Weird.txt'):
    print(os.stat(file).st_size)
    print(open(file,'r').read().upper())
SizeAndBig()
