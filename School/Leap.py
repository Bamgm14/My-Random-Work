#That ask user to enter a year and print out whether it is a leap year or not.
a=int(input("Enter Year:"))
b=a%4
if b==0:
    c=a%100
    if c==0:
        d=a%400
        if d==0:
            print ("Leap Year")
        else:
            print ("Not Leap Year")
    else:
        print ("Leap Year")
else:
    print ("Not Leap Year")
