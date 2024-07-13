def replace_last_value(tuples_list, new_value):
    return [t[:-1] + (new_value,) for t in tuples_list]


tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_value = 100
modified_list = replace_last_value(tuples_list, new_value)
print(f"Original list: {tuples_list}")
print(f"Modified list: {modified_list}")
