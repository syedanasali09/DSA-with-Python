my_list = []
num_items = int(input("Enter the number of items in the list: "))
for i in range(num_items):
    item = input("Enter an item for the list: ")
    my_list.append(item)

print("List before deletion:", my_list)
to_delete = input("Enter an item to delete from the list: ")

if to_delete in my_list:
    my_list.remove(to_delete)
    print(to_delete, "has been deleted from the list.")
else:
    print(to_delete, "is not found in the list.")

print("List after deletion:", my_list)

print("Items in the updated list:")
for item in my_list:
    print(item)