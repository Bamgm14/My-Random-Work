stack=[]
for x in range(int(input('Limit:'))):
    stack.append(input('Admin No:'))
for x in range(len(stack)):
    print(stack[x])
    if x<=10:
        print('Good Job '+stack[x]+'. You have earned 5 bonus points')
    else:
        print('Sorry '+stack[x]+' Better luck next time.')

