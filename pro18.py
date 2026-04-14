#18 Write a program which accepts a sequence of comma-separated umbers from console and generate a list and a tuple which contains every number.
#Enrollment no:92400527202

values = input("enter numbers separated comma: ")

lst = values.split(",")
tpl = tuple(lst)

print("list:", lst)
print("tuple:", tpl)
