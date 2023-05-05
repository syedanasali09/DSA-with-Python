class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				
        return item
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items

myStack = Stack()
print(myStack.push("A"))
print(myStack.push("B"))
print(myStack.push("C"))
myStack.push("D")
a= myStack.pop()
print (a)
print(myStack.peek())
