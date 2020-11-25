#To Write A Program Which Stores The Name Of Countries, Capital and Currency and Show it in Tabular for and print one specific country
Lmt=int(input('Enter Limit:'))
Dict={}
for x in range(Lmt):
    Cont=input('Enter Country:')
    Capt=input('Enter Capital:')
    Curr=input('Enter Currency:')
    Dict[Cont]=(Capt,Curr)
print('| Country | Capital | Currency |')
for x,y in Dict.items():
    print ('| '+x,end=' | ')
    for z in y:
        print (z,end=' | ')
    print('\n')
Sch=input('Enter Item To Search:')
if Sch in Dict.keys():
    print ('| '+Sch,end=' | ')
    for x in Dict[Sch]:
        print (x,end=' | ')
else:
    print('Country Not In Database')
