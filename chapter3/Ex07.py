arr = list(map(int, input("Nhập danh sách số: ").split()))
x = int(input("Nhập số cần tìm: "))

index = -1
for i in range(len(arr)):
    if arr[i] == x:
        index = i
        break

print("Chỉ số:", index)