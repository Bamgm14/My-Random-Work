import time
def encrypt1(char):
    cipher=''
    for x in char:
        if x==' ':
            cipher=cipher+x
        elif  x.isupper():
            cipher=cipher+chr((ord(x)+3-65)%26+65)
        else:
            cipher=cipher+chr((ord(x)+3-97)%26+97)
    return cipher
a=input("Enter PlainText:")
print (encrypt1(a))
