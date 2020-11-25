e=input("Enter File To Search(Make Sure To Be .txt):")
a=open(e,"r+")
b=a.read()
c=[]
d=''
for x in b:
    if x==" " or x=="\n":
        c.append(d)
        d=''
    else:
        d+=x
while '' in c:
    c.remove('')
f=input("Enter Term To Searched:")
g=0
if f in c:
    for x in c:
        if x==f:
            g+=1
    print ("Word Is Present",g,"Number Of Times")
else:
    print ("Word Isn't Present")

