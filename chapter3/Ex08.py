arr = list(map(int, input("Nhập danh sách số: ").split()))

found = None
for n in arr:
    if n > 10:
        found = n
        break

print("Số đầu tiên > 10:", found)