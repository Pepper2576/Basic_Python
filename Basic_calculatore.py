num1 = float(input('Please enter first number: '))
option = input('What would you like to do? +,-,*,/: ')
num2 = float(input('Please enter second number: '))
if option == '+':
    print(num1 + num2)
elif option =='-':
    print(num1 - num2)
elif option == '*':
    print(num1 * num2)
elif option == '/':
    if num2 == 0.0:
        print("Cannot divide by 0")
    else: 
        print(num1 / num2)
else:
    print('Please enter valid function')
