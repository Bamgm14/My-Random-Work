def Palin(e,d,f):
    while e<=d:
        if b[e]==b[d]:
            e+=1
            d-=1
        else:
            f=1
            break
    if f==0:
        print ("Palindrome")
    else:
        print ("Not Palindrome")
def Armstr(b,a,e):
    for x in b:
        x=int(x)
        e+=(x**3)
    if int(a)==e:
        print ("Armstrong")
    else:
        print ("Not  Armstrong")
a=input("Enter Number Or Word:")
b=[]
c=len(a)
d=c-1
e=0
f=0
g=""
for x in a:
    b.append(x)
if a.isalpha():
    g="P"
else:
    g=input("Choose Palindrome(P) Or Armstrong(A):")
if g=="P" or g=="p":
    Palin(e,d,f)
else:
    Armstr(b,a,e)
