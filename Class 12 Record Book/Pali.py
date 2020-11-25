def Pali(key='AmmA'):
    if key=='':
        return 'True'
    elif key[0]==key[len(key)-1]:
        return Pali(key[1:len(key)-1])
    else:
        return 'False'
print(Pali())
