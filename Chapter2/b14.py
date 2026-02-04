n = int(input("Nhập số n: "))

if n < 2:
    print(n, "không phải là số nguyên tố")
else:
    la_nguyen_to = True
    for i in range(2, n):
        if n % i == 0:
            la_nguyen_to = False
            break

    if la_nguyen_to:
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")

input("Nhấn Enter để thoát...")
