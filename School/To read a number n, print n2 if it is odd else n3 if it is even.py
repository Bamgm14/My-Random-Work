#To read a number n, print n2 if it is odd else n3 if it is even.
a=int(input("Enter Number:"))
b=a%2
if b==1:
    print (a**3)
else:
    print (a**2)
