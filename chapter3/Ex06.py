arr = list(map(int, input("Nhập danh sách số: ").split()))
swap = 0

for i in range(len(arr)):
    for j in range(len(arr)-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swap += 1

print("Danh sách sau khi sắp xếp:", arr)
print("Số lần hoán đổi:", swap)