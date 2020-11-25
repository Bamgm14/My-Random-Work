import math as m
b=.5
print (b)
a=int(input("Enter Limit:"))
for x in range(3,a,2):
    b=b*(x/x+1)*(x/x-1)
    print (b)
print (b)
