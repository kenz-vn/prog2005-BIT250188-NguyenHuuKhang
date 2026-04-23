from matplotlib import pyplot as plt
import numpy as np
x = np.arange(-5, 5, 0.0001)
y = x**2
z = x**3

plt.figure(figsize=(5.5, 2))
plt.subplot(1, 2, 1)  # 1 hàng, 2 cột, biểu đồ đầu tiên
plt.plot(x, y, 'b')  # Biểu đồ màu xanh
plt.subplot(1, 2, 2)  # 1 hàng, 2 cột, biểu đồ thứ hai
plt.plot(x, z, 'r')  # Biểu đồ màu đỏ
plt.show()