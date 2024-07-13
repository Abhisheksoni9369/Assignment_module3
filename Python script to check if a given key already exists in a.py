def key_exists_in_dict(d, key):
    return key in d


my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_check = 'b'
key_not_in_dict = 'z'


exists = key_exists_in_dict(my_dict, key_to_check)
not_exists = key_exists_in_dict(my_dict, key_not_in_dict)

print(f"Dictionary: {my_dict}")
print(f"Does the key '{key_to_check}' exist in the dictionary? {exists}")
print(f"Does the key '{key_not_in_dict}' exist in the dictionary? {not_exists}")
