a=[]
while True:
    b=input('Enter Number(Use String To Break):')
    if b.isalpha():
        break
    else:
        a.append(int(b))
b=int(input('Enter Number Freq:'))
c=0
for x in a:
    if b==x:
        c+=1
print ('Number Searched',b,'\nFreq',c)
