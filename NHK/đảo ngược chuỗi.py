s = input("Nhập chuỗi: ")
dao_nguoc = ""
for i in range(len(s) -1, -1, -1):
    dao_nguoc += s[i]
print("Chuỗi đảo ngược là:", dao_nguoc)