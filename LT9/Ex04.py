s = input("Nhập chuỗi: ")

upper = lower = digit = special = space = vowel = consonant = 0
vowels = "aeiouAEIOU"

for c in s:
    if c.isupper():
        upper += 1
    elif c.islower():
        lower += 1

    if c.isdigit():
        digit += 1
    elif not c.isalnum() and not c.isspace():
        special += 1

    if c.isspace():
        space += 1

    if c.isalpha():
        if c in vowels:
            vowel += 1
        else:
            consonant += 1

print("In hoa:", upper)
print("In thường:", lower)
print("Chữ số:", digit)
print("Ký tự đặc biệt:", special)
print("Khoảng trắng:", space)
print("Nguyên âm:", vowel)
print("Phụ âm:", consonant)