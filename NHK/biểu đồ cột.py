from matplotlib import pyplot as plt

categories = ['Excellent', 'Good', 'Average', 'Weak', 'Poor']
values = [25, 55, 10, 6, 4]

plt.bar(categories, values)
plt.title("Student Performance Classification")
plt.xlabel("Performance Level")
plt.ylabel("Number of Students")
plt.show()