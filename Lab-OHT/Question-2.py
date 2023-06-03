#use enqueue method to create the queue and fill the it with user defined element  
#implement display function for the queue  
#implement dequeue method to remove elements from the front of the queue
#use dequeue method to remove the first 3 elements from the queue 
#use the display a function again to display the edited queue
#implement a function is empty which checks if the queue is empty or not 
#step g. call the is empty function in the main method
#implement a while loop in the main method to dequeue all the element 
#now repeat step  g
#then display the queue again this should now appropriately display the the list is empty 

class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def display(self):
        if not self.is_empty():
            print("Queue:", self.queue)
        else:
            print("Queue is empty")

# Creating a queue and filling it with user-defined elements
queue = Queue()

print("Step 1: Create and fill the queue with user-defined elements")

for i in range(6):
    element = input(f"Enter element {i+1}: ")
    queue.enqueue(element)

# Displaying the queue
queue.display()

# Removing first 3 elements from the queue using dequeue
print("\nRemoving first 3 elements from the queue")
for _ in range(3):
    queue.dequeue()

# Displaying the edited queue
queue.display()

# Checking if the queue is empty using is_empty method
print("\nIs the queue empty?", queue.is_empty())

# Removing all elements from the queue using a while loop
print("\nRemoving all elements from the queue:")
while not queue.is_empty():
    print("Dequeued element:", queue.dequeue())

# Repeating Step 1: Create and fill the queue with user-defined elements
print("\nRepeating Step 1: Create and fill the queue with user-defined elements")
for i in range(6):
    element = input(f"Enter element {i+1}: ")
    queue.enqueue(element)

# Displaying the queue after repeating Step 1
queue.display()

