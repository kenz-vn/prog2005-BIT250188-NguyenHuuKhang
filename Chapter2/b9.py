n = input("Nhập số nguyên dương 5 chữ số: ")

max_digit = n[0]
for ch in n:
    if ch > max_digit:
        max_digit = ch

print("Chữ số lớn nhất là:", max_digit)

input("Nhấn Enter để thoát...")

