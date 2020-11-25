#To compute simple interest and compound interest.
a=float(input("Principal:"))
b=float(input("Annual Interest Rate:"))
c=float(input("Time(In Years):"))
d=int(input("Number Of Times Interest Is Compounded:"))
print ("Simple Interest:",(a*b*c))
print ("Compound Interest:",(a*(1+(b/d))**(d*c)))
