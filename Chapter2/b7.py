a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

while a != b:
    if a > b:
        a -= b
    else:
        b -= a

print("Ước số chung lớn nhất là:", a)

input("Nhấn Enter để thoát...")
