sum = 0
count = 0

while count < 10:
    num = int(input("Enter an integer: "))
    sum += num
    count += 1

average = sum / 10
print("Average value of 10 integers entered: ", average)