#To accepts marks in 5 subjects and displays the total and average mark
#Above 90%      Grade A*
#90 - 80 %      Grade A
#70 – 80 %    	Grade B
#60 – 70 %   	Grade C
#Less than 60   Grade D

a=float(input("Enter Mark(1):"))
b=float(input("Enter Mark(2):"))
c=float(input("Enter Mark(3):"))
d=float(input("Enter Mark(4):"))
e=float(input("Enter Mark(5):"))
f=(a+b+c+d+e)/5
if f>=90:
    print ("A+")
elif f<90 and f>=80:
    print ("A")
elif f<80 and f>=70:
    print ("B")
elif f<70 and f>=60:
    print ("C")
else:
    print ("D")
