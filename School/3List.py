def a(n,num):
    for x in range(3):
        n.append(int(input("Enter number for List "+str(num)+':')))
l1 = []
l2 = []
l3 = []
a(l1,1)
a(l2,2)
a(l3,3)
newlist=[]
for x in range(3):
    newlist.append(l1[x]+l2[x]+l3[x])
print ("New List:",newlist)
        
