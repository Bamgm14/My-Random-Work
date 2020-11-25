def HCF(num1,num2):
    if num1==0:
        return num2
    elif num2==0:
        return num1
    elif num1>num2:
        return HCF(num2,(num1%num2))
    elif num2>num1:
        return HCF(num1,(num2%num1))
print(HCF(56,18))
