from matplotlib import pyplot as plt

A = [1, 2, 3, 6, 10]
B = [4, 4, 7, 8, 8]
C = [9, 3, 4, 5, 6]

plt.plot(A, B, 'b', label='blue points')  # Đường màu xanh
plt.plot(C, B, 'r', label='red points')  # Đường màu đỏ
plt.title("Graph Title")  # Tiêu đề biểu đồ
plt.xlabel("Horizontal Axis")  # Nhãn trục hoành
plt.ylabel("Vertical Axis")  # Nhãn trục tung
plt.show()  # Hiển thị biểu đồ