def Fib(n,Fibi=[0,1]):
    if n<=1:
        return Fibi
    else:
        Fibi.append(Fibi[(len(Fibi))-2]+Fibi[(len(Fibi))-1])
        return Fib(n-1,Fibi)

