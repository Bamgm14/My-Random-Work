import time
def encrypt_1(message,s):
    ct=''
    for c in message:
        if c.isalpha():
            if c.isupper():
                ct += chr((ord(c)+s-65)%26+65)
            else:
                ct += chr((ord(c)+s-97)%26+97)
        else:
            ct+=c
    return ct
def encrypt_2(message,s):
    ct=[]
    for c in message:
        ct.append(ord(c)^s)
    return ct
str1 = input("Enter message:")
str1 = encrypt_1(str1,len(str1)%14)
str1 = encrypt_2(str1,len(str1))
for x in str1:
    x=hex(x)
    x=x[2:]
    print('\\x'+x,end='')
time.sleep(10)
