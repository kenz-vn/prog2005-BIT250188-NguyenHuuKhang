s = input("Nhập chuỗi: ")
nums = [int(x.strip()) for x in s.split(";")]

for n in nums:
     print(n)

chan = sum(1 for n in nums if n%2 == 0)
am = sum(1 for n in nums if n < 0)

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
        return True

nguyen_to = sum(1 for n in nums if prime(n))

tb = sum(nums) / len(nums)

print("Số chẵn: ", chan)
print("Số âm: ", am)
print("Số nguyên tố: ", nguyen_to)
print("Trung bình:", tb

