#20 Write a program to read names from keyboard and store into text file
#Enrollment no:92400527202
f = open("names.txt", "w")

n = int(input("how many names: "))

for i in range(n):
    name = input("enter name: ")
    f.write(name + "\n")

f.close()
print("names saved successfully")
