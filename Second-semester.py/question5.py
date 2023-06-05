def calculate_statistics():
    numbers = []  # Empty list to store the numbers

    # Take input from the user
    n = int(input("Enter the number of elements: "))

    # Take n numbers as input
    for i in range(n):
        num = float(input("Enter a number: "))
        numbers.append(num)

    # Calculate sum
    total = sum(numbers)

    # Calculate average
    average = total / n

    # Find the smallest and largest values
    smallest = min(numbers)
    largest = max(numbers)

    # Print the results
    print("Sum: ", total)
    print("Average: ", average)
    print("Smallest value: ", smallest)
    print("Largest value: ", largest)


# Call the function to run the program
calculate_statistics()
