try:
    a = int(input("Nhap so thu nhat: "))
    b = int(input("Nhap so thu hai: "))

    result = a / b
    print("Ket qua chia:", result)

except ZeroDivisionError:
    print("Loi: Khong the chia cho 0")

except ValueError:
    print("Loi: Ban phai nhap so nguyen hop le")