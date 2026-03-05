arr = list(map(int, input("Nhập danh sách số: ").split()))

total = 0
print("Các số chẵn:")

for n in arr:
    if n % 2 == 0:
        print(n)
        total += n

print("Tổng số chẵn:", total)