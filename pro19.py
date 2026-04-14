#19 Write a Python Program to create a function which accepts 3 arguments. (2 numbers and one arithmetic operator). Display answer accordingly.
#Enrollment no:92400527202

def calculate(a, b, op):
    if op == '+':
        print("answer:", a + b)
    elif op == '-':
        print("answer:", a - b)
    elif op == '*':
        print("answer:", a * b)
    elif op == '/':
        if b != 0:
            print("answer:", a / b)
        else:
            print("division not possible")
    else:
        print("invalid operator")

x = int(input("enter first number: "))
y = int(input("enter second number: "))
operator = input("enter operator (+, -, *, /): ")

calculate(x, y, operator)
