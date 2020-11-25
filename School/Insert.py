def insertionsort(array):
    for x in range(1,len(array)):
        key = array[x]
        j = x - 1
        while ( j >= 0 and key < array[j]):
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key

    return array
l = []

 
for x in range(int(input("Enter no. of data: "))):
    l.append(int(input("Enter data: ")))

print("Initial List; ", l)
insertionsort(l)

print("Sorted List: ",l)
