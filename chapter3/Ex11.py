arr = list(map(int, input("Nhập các số: ").split()))

max_val = arr[0]
min_val = arr[0]

for n in arr:
    if n > max_val:
        max_val = n
    if n < min_val:
        min_val = n

print("Số lớn nhất:", max_val)
print("Số nhỏ nhất:", min_val)