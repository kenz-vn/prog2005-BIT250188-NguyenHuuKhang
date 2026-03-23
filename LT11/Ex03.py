nums = list(map(int, input("Nhập các số: ").split()))
even_nums = []
total = 0
for n in nums:
    if n % 2 == 0:
        even_nums.append(n)
        total += n
print("Các số chẵn:", even_nums)
print("Tổng các số chẵn:", total)