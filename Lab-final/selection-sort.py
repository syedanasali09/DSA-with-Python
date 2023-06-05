def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
numbers = [7, 3, 1, 9, 5]
selection_sort(numbers)
print(numbers)  # Output: [1, 3, 5, 7, 9]
