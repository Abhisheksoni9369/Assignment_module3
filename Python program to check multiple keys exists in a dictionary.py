def check_keys_exist(d, keys):
    return all(key in d for key in keys)


my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys_to_check = ['a', 'c']
keys_not_in_dict = ['a', 'z']


keys_exist = check_keys_exist(my_dict, keys_to_check)
keys_not_exist = check_keys_exist(my_dict, keys_not_in_dict)

print(f"Dictionary: {my_dict}")
print(f"Do the keys {keys_to_check} exist in the dictionary? {keys_exist}")
print(f"Do the keys {keys_not_in_dict} exist in the dictionary? {keys_not_exist}")
