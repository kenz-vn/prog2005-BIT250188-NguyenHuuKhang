def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Ví dụ danh sách 5 chuỗi đã sắp xếp
arr = ["apple", "banana", "mango", "orange", "peach"]
print("Danh sách chuỗi:", arr)
x = input("Nhập chuỗi cần tìm: ")
kq = binary_search(arr, x)
if kq != -1:
    print("Tìm thấy tại vị trí:", kq + 1)
else:
    print("Không tìm thấy")