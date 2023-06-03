
class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"
        
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def display(self):
        if not self.is_empty():
            print("Stack:", self.stack)
        else:
            print("Stack is empty")

# Creating a stack and filling it with user-defined elements
stack = Stack()

print("Step 1: Create and fill the stack with user-defined elements")

for i in range(6):
    element = input(f"Enter element {i+1}: ")
    stack.push(element)

# Displaying the stack
stack.display()

# Removing first 3 elements from the stack using pop
print("\nRemoving first 3 elements from the stack")
for _ in range(3):
    stack.pop()

# Displaying the edited stack
stack.display()

# Checking the element at the top of the stack using top method
print("\nElement at the top of the stack:", stack.top())

# Checking if the stack is empty using is_empty method
print("Is the stack empty?", stack.is_empty())

# Removing all elements from the stack using a while loop
print("\nRemoving all elements from the stack:")
while not stack.is_empty():
    print("Element at the top of the stack:", stack.top())
    stack.pop()

# Repeating Step 1: Create and fill the stack with user-defined elements
print("\nRepeating Step 1: Create and fill the stack with user-defined elements")
for i in range(6):
    element = input(f"Enter element {i+1}: ")
    stack.push(element)

# Displaying the stack after repeating Step 1
stack.display()

