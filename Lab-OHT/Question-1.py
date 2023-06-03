#create a sequence of list which takes input from the user and apply selection sort to sort that list.

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

# Taking input from the user to create a list
num = int(input("Enter the number of elements in the list: "))
input_list = []

for i in range(num):
    element = int(input(f"Enter element {i+1}: "))
    input_list.append(element)

# Sorting the list using selection sort
sorted_list = selection_sort(input_list)

# Displaying the sorted list
print("Sorted list:", sorted_list)

