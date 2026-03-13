n = int(input("Enter number: "))

fact = 1

if n < 0:
    print("Factorial not possible")
else:
    for i in range(1, n+1):
        fact = fact * i

    print("Factorial is", fact)

