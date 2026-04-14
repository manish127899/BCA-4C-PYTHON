#26 Python program of Barplot with all parameters of a sample data
#Enrollment no:92400527202

import matplotlib.pyplot as plt

subjects = ["maths", "science", "english", "computer"]
marks = [80, 70, 90, 85]

plt.bar(subjects, marks, color="skyblue", width=0.5)

plt.title("student Marks Bar Chart")
plt.xlabel("subjects")
plt.ylabel("marks")

plt.show()
