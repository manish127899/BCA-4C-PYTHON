#29 Python program of Box Plot with all parameters of a sample data.
#Enrolment no:92400527202

import matplotlib.pyplot as plt

data = [10, 20, 30, 40, 50, 60, 70, 80]

plt.boxplot(data, patch_artist=True)

plt.title("box plot example")
plt.ylabel("values")

plt.show()
