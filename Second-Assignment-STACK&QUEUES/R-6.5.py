def reverse_list_using_stack(lst):
    stack = []
    for element in lst:
        stack.append(element)  

    lst.clear()  

    while stack:
        lst.append(stack.pop())  

user_input = input("Enter space-separated elements for the list: ")
lst = user_input.split()

print("List before reversal:", lst)
reverse_list_using_stack(lst)
print("List after reversal:", lst)