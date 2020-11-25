def Fact(n):
    if n<1:
        return 1
    else:
        return (n*Fact(n-1))
print(Fact(5))
def HCF(num1,num2):
    if num1==0:
        return num2
    elif num2==0:
        return num1
    elif num1>num2:
        return HCF(num2,(num1%num2))
    elif num2>num1:
        return HCF(num1,(num2%num1))
print(HCF(25,15))
def Fib(n,Fibi=[0,1]):
    if n<=1:
        return Fibi
    else:
        Fibi.append(Fibi[(len(Fibi))-2]+Fibi[(len(Fibi))-1])
        return Fib(n-1,Fibi)
print(Fib(5))
def List(lst,n=0,value=0):
    if len(lst)==n:
        return value
    else:
        value+=lst[n]
        return List(lst,n+1,value)
print(List([1,23,4,5,6,24,56,3,5,53,5]))
def Pali()
