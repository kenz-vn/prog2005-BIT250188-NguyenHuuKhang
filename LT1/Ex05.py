import random

m = int(input("M: "))
n = int(input("N: "))

a = [[random.randint(1,100) for j in range(n)] for i in range(m)]

for row in a:
    print(row)

h = int(input("Hàng muốn xem: "))
print("Hàng:", a[h-1])

c = int(input("Cột muốn xem: "))
for i in range(m):
    print(a[i][c-1])

print("Max:", max(max(row) for row in a))