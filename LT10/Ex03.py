def factorial(n):
    if n == 0 or n == 1:   # điều kiện dừng
        return 1
    return n * factorial(n - 1)

# Nhập dữ liệu
n = int(input("Nhập số: "))

if n < 0:
    print("Không có giai thừa cho số âm")
else:
    print("Giai thừa =", factorial(n))