def List(lst,n=0,value=0):
    if len(lst)==n:
        return value
    else:
        value+=lst[n]
        return List(lst,n+1,value)
print(List([1,23,4,5,6,24,56,3,5,53,5]))
