n=3
row=1
while row<=n:
    col=1
    sp=0
    while sp<=n-row:
        print(' ',end=' ')
        sp+=1
    while col<=row:
        print("*  ",end=' ')
        col+=1
    row+=1
    print()
    
