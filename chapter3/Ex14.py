def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for c in s:
        if c in vowels:
            count += 1

    return count

text = input("Nhập chuỗi: ")
print("Số nguyên âm:", count_vowels(text))