class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j].age > arr[j + 1].age:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
students = [
    Student("Alice", 20),
    Student("Bob", 18),
    Student("Charlie", 22),
    Student("David", 19),
]
bubble_sort(students)
for student in students:
    print(student)
