def is_list_empty(lst):
    return len(lst) == 0

list1 = []
list2 = [1, 2, 3]

print(f"Is list1 empty? {'Yes' if is_list_empty(list1) else 'No'}")
print(f"Is list2 empty? {'Yes' if is_list_empty(list2) else 'No'}")
