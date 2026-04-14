#28 Python program of Line plot with all parameters of a sample data.
#Enrollment no:92400527202

import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sales = [100, 150, 120, 170, 200]

plt.plot(days, sales, color="green", marker="o", linestyle="--")

plt.title("daily sales")
plt.xlabel("days")
plt.ylabel("sales")

plt.grid(True)

plt.show()
