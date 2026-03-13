age = int(input("Enter your age: "))

if age < 12:
    print("You are Kid")
elif age >= 12 and age <= 17:
    print("You are Teenager")
elif age >= 18 and age <= 60:
    print("You are Adult")
else:
    print("You are Senior Citizen")
