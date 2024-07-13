def map_lists_to_dict(keys, values):
    return dict(zip(keys, values))


keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]

mapped_dict = map_lists_to_dict(keys, values)

print("Keys list:", keys)
print("Values list:", values)
print("Mapped dictionary:", mapped_dict)
