def palin(n):
    n1=n
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if rev==n1:
        print("Palindrome")
    else:
        print("Not Palindrome")

def armst(n):
    n1=n
    ar=0
    while n>0:
        rem=n%10
        ar=ar+rem**3
        n=n//10
    if ar==n1:
        print("Armstrong")
    else:
        print("Not Armstrong")
        
a=int(input("Enter a number:"))
p=int(input("Enter 1 for palindrome or 2 for armstrong:"))
if p==1:
    palin(a)
if p==2:
    armst(a)
