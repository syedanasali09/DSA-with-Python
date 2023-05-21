class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


def decimal_to_binary(decimal):
    stack = Stack()

    while decimal > 0:
        remainder = decimal % 2
        stack.push(remainder)
        decimal = decimal // 2

    binary = ""
    while not stack.is_empty():
        binary += str(stack.pop())

    return binary



decimal_number = 10
binary_number = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is: {binary_number}")
