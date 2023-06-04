#what values are returned during the following series of stack operations 
# if execueted upon an initially empty stack?
#push(5),push(3),pop(),push(2),push(8),pop(),pop(),
#push(9)push(1),pop(),push(7),push(6),)pop(),pop(),push(4),pop(),pop().

class Stack:
    def __init__(self):
        self.items = []  

    def push(self,item):
         self.items.append(item)
         
    def pop(self):
        return self.item.pop()
    
    def __str__(self):
        return str(self.items)
    
s = Stack()
s.push(5)
s.push(3)
s.pop()
s.push(2)
s.push(8)
s.pop()
s.pop()
s.push(9)
s.push(1)
s.pop()
s.push(7)
s.push(6)
s.pop()
s.pop()
s.push(4)
s.pop() 
s.pop()
 
print(s)
        
      