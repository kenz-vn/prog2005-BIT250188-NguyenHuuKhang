arr = []
for i in range(5):
    arr.append(input(f"Chuỗi {i+1}: "))

n = len(arr)

for i in range(n):
    for j in range(n - i - 1):
        if len(arr[j]) < len(arr[j+1]):
            arr[j], arr[j+1] = arr[j+1], arr[j]
            print(arr)