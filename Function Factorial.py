def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

number = int(input("Enter a number: "))

if number < 0:
    print("Factorial does not exist for negative numbers.")
else:
    result = factorial(number)
    print("Factorial of", number, "is", result)
