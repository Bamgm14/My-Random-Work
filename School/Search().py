def ab(b):
    c=input("Term To Be Search:")
    if c in b:
        print ("Term Found")
    else:
        print ("Term Not Found")
a=[]
while True:
    b=input("Enter Term(To terminate type Exit):")
    if b=='Exit' or b=='exit':
        break
    else:
        a.append(b)
ab(a)

