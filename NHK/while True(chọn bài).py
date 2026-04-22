def bai1():
    print("Bài 1: Tính tổng 2 số")
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    print("Tổng =", a + b)

def bai2():

def bai3():
    print("Bài 3: Đảo ngược chuỗi")
    s = input("Nhập chuỗi: ")
    print("Chuỗi đảo ngược:", s[::-1])

def bai4():
    print("Bài 4: Kiểm tra số chẵn/lẻ")
    n = int(input("Nhập số: "))
    if n % 2 == 0:
        print("Số chẵn")
    else:
        print("Số lẻ")

while True:
    try:
        chon = int(input("Chọn bài (1-4, 0 để thoát): "))
    except:
        print("Vui lòng nhập số!")
        continue

    if chon == 1:
        bai1()
    elif chon == 2:
        bai2()
    elif chon == 3:
        bai3()
    elif chon == 4:
        bai4()
    elif chon == 0:
        print("Thoát chương trình")
        break
    else:
        print("Chọn sai!")