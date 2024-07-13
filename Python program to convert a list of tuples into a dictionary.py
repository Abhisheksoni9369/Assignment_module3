def list_of_tuples_to_dict(tuples_list):
    return dict(tuples_list)


my_list_of_tuples = [(1, 'one'), (2, 'two'), (3, 'three')]
converted_dict = list_of_tuples_to_dict(my_list_of_tuples)
print(f"Original list of tuples: {my_list_of_tuples}")
print(f"Converted dictionary: {converted_dict}")
