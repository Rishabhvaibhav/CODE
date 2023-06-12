num1 = eval(input("Enter first number: "))
num2 = eval(input("Enter second number: "))
oper = input("Enter operator: ")

if oper == '+':
    print(num1+num2)
elif oper == '-':
    print(num1-num2)
elif oper == '*':
    print(num1*num2)
elif oper == '/':
    print(num1/num2)
else:
    print("Invalid operator")

