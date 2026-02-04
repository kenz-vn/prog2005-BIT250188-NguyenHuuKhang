n = int(input("Nhập số dương: "))

dao_nguoc = 0
while n > 0:
    dao_nguoc = dao_nguoc * 10 + n % 10
    n //= 10

print("Số sau khi đảo ngược:", dao_nguoc)

input("Nhấn Enter để thoát...")

