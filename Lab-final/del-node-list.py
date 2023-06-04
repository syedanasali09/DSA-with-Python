# Deleting a node from the linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next


my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)


my_list.delete(2)


my_list.display()
