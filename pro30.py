#30 Python program of Scatter Plot with all parameters of a sample data.
#Enrollment no:92400527202

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.scatter(x, y, color="red", marker="o")

plt.title("Scatter Plot Example")
plt.xlabel("X values")
plt.ylabel("Y values")

plt.show()
