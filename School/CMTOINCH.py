#That ask the user to enter a length in cm. if the user enter a negative value the program should tell the user â€œThe entry is invalidâ€, otherwise the program should convert length to inches and print out the result [Hint  2.5cm = 1 inch]
a=float(input("Enter Lenght in Centimeter:"))
if a<0:
    print ("This Entry Is Not Valid")
else:
    b=a*2.5
    print ("Value In Inches:",b)
