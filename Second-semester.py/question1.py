def add_arrays(A, B, m, n):
    result = [[0] * n for _ in range(m)]  # Create an empty result array

    for i in range(m):
        for j in range(n):
            result[i][j] = A[i][j] + B[i][j]  # Add corresponding elements from A and B

    return result

# Input the size of the arrays
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

# Input elements of array A
print("Enter elements of array A:")
A = []
for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"Enter element [{i}][{j}]: "))
        row.append(element)
    A.append(row)

# Input elements of array B
print("Enter elements of array B:")
B = []
for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"Enter element [{i}][{j}]: "))
        row.append(element)
    B.append(row)

# Add arrays A and B
result = add_arrays(A, B, m, n)

# Print the result
print("Sum of arrays A and B:")
for row in result:
    print(row)