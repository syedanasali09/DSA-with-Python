def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        
        for j in range(n - i - 1):
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

arr = [64, 25, 12, 22, 11]
sorted_arr = bubble_sort(arr)
print(sorted_arr)

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
       
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

arr = [4, 25, 15, 12, 11]
sorted_arr = selection_sort(arr)
print(sorted_arr)