n = int(input("Enter number: "))

count = 0

if n <= 1:
    print("Not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            count = 1
            break

    if count == 0:
        print("Prime Number")
    else:
        print("Not Prime")
