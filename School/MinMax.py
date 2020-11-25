def minmax(li):
    for x in li:
        flag = 0
        for y in li:
            if x<=y:
                pass
            else:
                flag = 1
                break
        if flag == 0:
            print("Minimum element: ",x)
            break
        flag = 0
    for x in li:
        flag = 0
        for y in li:
            if x>=y:
                pass
            else:
                flag = 1
                break
        if flag == 0:
            print("Maximum element: ",x)
            break
        flag = 0

lists = []
while True:
    x = input("Enter number..")
    if ("exit" in  x):
        break
    else:
        lists.append(int(x))
minmax(lists)
