def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        max_index = i
        for j in range(i+1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]

arr = [1,2,3,4,5]
selection_sort(arr)
print("selection Sort:", arr)