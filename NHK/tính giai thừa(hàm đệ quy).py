def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)

n = int(input("Nhập số: "))

if n < 0:
    print("Không tính được giai thừa số âm")
else:
    print("Giai thừa là:", giai_thua(n))