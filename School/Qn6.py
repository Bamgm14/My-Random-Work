'''for x in range(1,10000000001):
    a=x**3
    b=x*(x**4-1)
    c=x**2
    d=(((c)+((a)**2))/((x*a)+1))
    e=((b*a)+1)
    f=((a)**2)+((b)**2)
    g=(f)/(e)
    print (x,a,b,c,d,e,f,g)
    if (c)==(d) and (c)==(g):
        print ('Second And Third True')
    elif (c)==(g):
        print ('Thrid True')
    elif (c)==(d):
        print ('Second True')
    else:
        print ('Failed')'''
a=[]
for z in range(1000):
    for y in range(1000):
        for x in range(1000):
            if (z**2)==((x**2)+(y**2))/((x*y)+1):
                b=(x,y,z)
                a.append(b)
print (a)
