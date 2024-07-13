def unique_values_in_dict(d):
    unique_values = set()
    for value in d.values():
        unique_values.add(value)
    return unique_values


my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

unique_values = unique_values_in_dict(my_dict)

print("Dictionary:", my_dict)
print("Unique values:", unique_values)
