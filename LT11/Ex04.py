def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
lst = list(map(int, input("Nhập danh sách số nguyên: ").split()))
print("Danh sách ban đầu:", lst)
x = int(input("Nhập phần tử cần thêm: "))
lst.append(x)
print("Sau khi thêm:", lst)
k = int(input("Nhập k: "))
count = lst.count(k)
print(f"Số lần xuất hiện của {k}:", count)
prime_sum = sum(n for n in lst if is_prime(n))
print("Tổng các số nguyên tố:", prime_sum)
lst.sort()
print("Danh sách sau khi sắp xếp:", lst)
lst.clear()
print("Danh sách sau khi xóa:", lst)