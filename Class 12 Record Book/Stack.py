stack=[]
for x in range(int(input('Limit:'))):
    stack.append(int(input('Number:')))
for x in range(len(stack)):
    print((stack.pop())**2)
