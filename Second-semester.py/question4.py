n = int(input("Enter the number of entities: "))

fib_series = [0, 1]

for i in range(2, n):
    fib_series.append(fib_series[i - 1] + fib_series[i - 2])

for num in fib_series:
    print(num, end=" ")