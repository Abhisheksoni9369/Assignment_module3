def create_dict_from_tuples(tuples_list):
    return dict(tuples_list)


tuples_list = [('a', 1), ('b', 2), ('c', 3)]
dictionary = create_dict_from_tuples(tuples_list)
print(f"List of tuples: {tuples_list}")
print(f"Created dictionary: {dictionary}")
