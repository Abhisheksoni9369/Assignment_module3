def remove_empty_tuples(tuples_list):
    return [tup for tup in tuples_list if tup]


my_list_of_tuples = [(1, 2), (), (3, 4, 5), (), (6, 7, 8, 9)]
filtered_list = remove_empty_tuples(my_list_of_tuples)
print(f"Original list: {my_list_of_tuples}")
print(f"Filtered list (without empty tuples): {filtered_list}")
