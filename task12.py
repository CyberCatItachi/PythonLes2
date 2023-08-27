num1 = int(input("Введите сумму цифр загаданного числа: "))
num2 = int(input("Введите произведение цифр загаданного числа: "))
D = num1 ** 2 - 4 * num2 
sqrtD = D ** 0.5 
root1 = (num1 - sqrtD)/2   
root2 = (num1 + sqrtD)/2 
print(round(root1), round(root2))
