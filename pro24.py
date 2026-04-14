#24 Write a Python Program that creates a class with function overloading
#Enrollment no:92400527202
class Demo:
    
    def add(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            print("sum of 3:", a + b + c)
        elif a != None and b != None:
            print("sum of 2:", a + b)
        else:
            print("invalid input")

d = Demo()

d.add(10, 20)
d.add(10, 20, 30)
