#16 Write a program to create list in such a way that it should add square roots of number between 1 to n in the list...At the end, the list shall be
#Enroolment no:9240052720

n = int(input("enter value of n: "))

lst = []

for i in range(1, n+1):
    lst.append(i*i)

print("list of squares:", lst)
