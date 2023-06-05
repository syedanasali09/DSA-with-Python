def input_matrix(matrix, m, n):
    print("Enter the elements of the matrix:")
    for i in range(m):
        row = []
        for j in range(n):
            element = int(input(f"Enter element [{i}][{j}]: "))
            row.append(element)
        matrix.append(row)

def display_matrix(matrix):
    print("Matrix:")
    for row in matrix:
        print(row)

def sum_of_elements(matrix):
    total_sum = 0
    for row in matrix:
        total_sum += sum(row)
    print("Sum of all elements:", total_sum)

def row_wise_sum(matrix):
    print("Row-wise sum:")
    for i, row in enumerate(matrix):
        row_sum = sum(row)
        print(f"Row {i+1}: {row_sum}")

def column_wise_sum(matrix):
    print("Column-wise sum:")
    num_columns = len(matrix[0])
    for j in range(num_columns):
        column_sum = sum(row[j] for row in matrix)
        print(f"Column {j+1}: {column_sum}")

def create_transpose(matrix):
    transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    print("Transpose of the matrix:")
    for row in transpose:
        print(row)

# Main program
matrix = []
m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))

while True:
    print("\nMenu:")
    print("a. Input elements into the matrix")
    print("b. Display elements of the matrix")
    print("c. Sum of all elements of the matrix")
    print("d. Display row-wise sum of the matrix")
    print("e. Display column-wise sum of the matrix")
    print("f. Create transpose of the matrix")
    print("q. Quit")

    choice = input("Enter your choice: ")

    if choice == "a":
        input_matrix(matrix, m, n)
    elif choice == "b":
        display_matrix(matrix)
    elif choice == "c":
        sum_of_elements(matrix)
    elif choice == "d":
        row_wise_sum(matrix)
    elif choice == "e":
        column_wise_sum(matrix)
    elif choice == "f":
        create_transpose(matrix)
    elif choice == "q":
        break
    else:
        print("Invalid choice. Please try again.")

print("Program exited.")