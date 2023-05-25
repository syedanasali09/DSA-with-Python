def remove_elements_from_stack(stack):
    if not stack:  
        return
    
    stack.pop()  
    remove_elements_from_stack(stack)  

user_input = input("Enter space-separated elements for the stack: ")
stack = user_input.split()

print("Stack before removal:", stack)
remove_elements_from_stack(stack)
print("Stack after removal:", stack)