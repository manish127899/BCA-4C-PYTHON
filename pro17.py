#17 Write a program to create dictionary in such a way that it should add number as a key and square root of number as a valuebetween 1 to n in the dictionary... At the end, the data shall be displayed.
#Enrollment no:92400527202

n = int(input("enter value of n: "))

d = {}

for i in range(1, n+1):
    d[i] = i*i

print("dictionary:", d)
