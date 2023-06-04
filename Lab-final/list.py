ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]


ages.sort()


min_age = ages[0]
max_age = ages[-1]

ages.append(min_age)
ages.append(max_age)


average_age = sum(ages) / len(ages)


print("Sorted Ages:", ages)
print("Minimum Age:", min_age)
print("Maximum Age:", max_age)
print("Average Age:", average_age)
