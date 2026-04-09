s = input("Nhập chuỗi: ")

hoa = thuong = so = db = space = na = pa = 0
vowels = "aeiouAEIOU"

for c in s:
    if c.isupper(): hoa += 1
    if c.islower(): thuong += 1
    if c.isdigit(): so += 1
    if c.isspace(): space += 1
    if not c.isalnum() and not c.isspace(): db += 1

    if c.isalpha():
        if c in vowels:
            na += 1
        else:
            pa += 1

print("Hoa:", hoa)
print("Thường:", thuong)
print("Số:", so)
print("Đặc biệt:", db)
print("Khoảng trắng:", space)
print("Nguyên âm:", na)
print("Phụ âm:", pa)