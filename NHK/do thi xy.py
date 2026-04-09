from matplotlib import pyplot as plt
import numpy as np

x = np.arange(-5, 5, 0.001)
y = x**3

plt.figure(figsize=(5, 2))
plt.plot(x, y, 'b')
plt.title("Function Plot y = x^3")
plt.xlabel("Horizontal Axis")
plt.ylabel("Vertical Axis")
plt.show()