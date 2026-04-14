#27 Python program of Pie-chart with all parameters of a sample data.
#Enrollment no:92400527202

import matplotlib.pyplot as plt

labels = ["maths", "dbms", "java", "dsa"]
marks = [80, 70, 90, 85]

plt.pie(marks, labels=labels, autopct="%1.1f%%", startangle=90)

plt.title("marks distribution")
plt.axis("equal")

plt.show()
