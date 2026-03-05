arr = list(map(int, input("Nhập danh sách số: ").split()))

print("Các số lẻ:")
for n in arr:
    if n % 2 != 0:
        print(n)