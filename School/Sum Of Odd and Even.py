a=int(input("Enter Number:"))
b=1
d=0
e=0
while b<=a:
    c=b%2
    if c==0:
        d+=b
    else:
        e+=b
    b+=1
print ("Sum of Even:",d)
print ("Sum Of Odd:",e)
