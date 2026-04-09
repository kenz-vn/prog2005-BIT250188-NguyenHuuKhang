from matplotlib import pyplot as plt

categories = ['Excellent', 'Good', 'Average', 'Weak', 'Poor']
values = [25, 55, 41, 30, 50]

plt.pie(values, labels=categories)
plt.title("Pie Chart")
plt.show()