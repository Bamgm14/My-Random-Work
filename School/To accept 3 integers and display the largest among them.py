#To accept 3 integers and display the largest among them
a=int(input("Enter Number:"))
b=int(input("Enter Number:"))
c=int(input("Enter Number:"))
if a>b and a>c:
    print (a,"is greater")
elif a<b and b>c:
    print (b,"is greater")
elif a<c and b<c:
    print (c,"is greater")
elif a>b and a==c:
    print (a,"and",c,"are greater")
elif a>c and a==b:
    print (a,"and",b,"are greater")
elif c>a and a==b:
    print (b,"and",c,"are greater")
else:
    print ("All 3 are equal")
