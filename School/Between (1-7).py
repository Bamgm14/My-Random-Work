#To accept a single digit Between (1-7) and display a 3 digit number as n*100+(n+1)*10+(n+2))
while True:
    a=int(input("Enter Number(n):"))
    if a>7 or a<1:
        print ("INPUT NUMBER BETWEEN 1 AND 7")
    else:
        b=(a+1)*10
        c=(a+2)
        a=a*100
        print (a+b+c)
        break
    
