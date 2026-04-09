def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i #max_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]: #if arr[j] > arr[max_index]
                min_index = j #max_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i] #arr[i], arr[max_index] = arr[max_index], arr[i]

# Ví dụ sử dụng
arr1 = [64, 25, 12, 22, 11]
selection_sort(arr1)
print("Selection Sort:", arr1)

