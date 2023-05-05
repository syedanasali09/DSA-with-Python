def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = arr[j+1], arr[j]


array = input("Enter numbers to sort: ")
array = list(map(int, array.split()))


bubble_sort(array)


print("Sorted array:", array)
