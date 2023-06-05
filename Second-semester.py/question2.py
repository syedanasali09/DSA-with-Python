num = int(input("Enter an integer: "))

# Convert the integer to a string and reverse it
num_str = str(num)
reversed_str = num_str[::-1]

# Convert the reversed string back to an integer
reversed_num = int(reversed_str)

print("Reversed number:", reversed_num)