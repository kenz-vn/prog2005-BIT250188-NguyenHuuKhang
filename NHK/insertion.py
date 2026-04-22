def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] > key: # < key
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
arr = [64,23,43,55,76,23]
insertion_sort(arr)
print("insertion Sort: ",arr)]