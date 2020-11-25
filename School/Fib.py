def fib(nterms):
    fibseries=[0,1]
    for x in range(2,nterms):
        fibseries.append(fibseries[x-1]+fibseries[x-2])
    return fibseries
nterms=int(input('Enter number of terms:'))
print(fib(nterms))
