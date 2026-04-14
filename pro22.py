#22 Write a program to read text file having number and display all numbers with total and average at the last. (Manually prepare a file having some numbers and then read it)
#Enrollment no:92400527202
f = open("numbers.txt", "r")

data = f.read()
nums = data.split()

total = 0

for n in nums:
    total += int(n)

avg = total / len(nums)

print("total:", total)
print("average:", avg)

f.close()
