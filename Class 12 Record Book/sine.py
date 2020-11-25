import math as m
def SinAndCompare(value=m.pi/4,acc=50):
    ans=0
    for x in range(acc):
        ans+=(((-1)**(x))*((value)**(2*x+1)))/(m.factorial(2*x+1))
    print(ans)
    print(m.sin(value))
SinAndCompare()
