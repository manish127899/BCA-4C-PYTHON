print("Enter marks of 4 subjects:")

sub1 = int(input("Subject 1: "))
sub2 = int(input("Subject 2: "))
sub3 = int(input("Subject 3: "))
sub4 = int(input("Subject 4: "))

total = sub1 + sub2 + sub3 + sub4
percentage = total / 4

print("Total Marks =", total)
print("Percentage =", percentage)

# Check result
if sub1 < 40 or sub2 < 40 or sub3 < 40 or sub4 < 40:
    print("Result = FAIL")
    print("Grade = With Held")
else:
    print("Result = PASS")
    
    if percentage >= 75:
        print("Grade = Distinction")
    elif percentage >= 60:
        print("Grade = First Class")
    elif percentage >= 50:
        print("Grade = Second Class")
    else:
        print("Grade = Pass")
