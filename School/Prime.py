a=int(input("Enter Number:"))
c=0
if a<2:
    print ("No Number Below 2 Is Prime")
    exit
else:
    b=2
    while b<a:
        if a%b!=0:
            b+=1
            continue
        else:
            c=b
            break
if c==0:
    print ("Prime")
else:
    print ("Not Prime and divisible by",c)
