def get_unique_values(lst):
    unique_values = list(set(lst))
    return unique_values


my_list = [1, 2, 2, 3, 4, 4, 5]
unique_values = get_unique_values(my_list)
print(f"Original list: {my_list}")
print(f"Unique values: {unique_values}")
