#ý 1
for i in range(111, 16, -1):
    if i % 2 != 0:
        print(i, end=" ")


#ý 2
for n in range(17, 112):
    la_so_nguyen_to = True
    if n < 2:
        la_so_nguyen_to = False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                la_so_nguyen_to = False
                break
    if la_so_nguyen_to:
        print(n, end=" ")
