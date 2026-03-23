arr = []
for i in range(5):
    s = input(f"Nhập chuỗi thứ {i+1}: ")
    arr.append(s)
arr.sort()
print("\nDanh sách sau sắp xếp:", arr)
target = input("Nhập chuỗi cần tìm: ")
left = 0
right = len(arr) - 1
found = False
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        print(f"Tìm thấy tại vị trí: {mid}")
        found = True
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
if not found:
    print("Không tìm thấy chuỗi!")