n = int(input("Nhập số n: "))

a, b = 0, 1
print("Dãy Fibonacci:")

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

input("Nhấn Enter để thoát...")
