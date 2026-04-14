#21 Write a program to read any text file line by line
#Enrollment no:92400527202
f = open("names.txt", "r")

for line in f:
    print(line.strip())

f.close()
