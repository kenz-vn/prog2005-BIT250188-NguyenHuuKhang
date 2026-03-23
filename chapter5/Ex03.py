from matplotlib import pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [30,25,15,20,10]

plt.pie(values, labels=categories)
plt.title('pie chart')
plt.show()
