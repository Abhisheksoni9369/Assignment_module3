dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

def concatenate_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result


new_dict = concatenate_dicts(dict1, dict2, dict3)
print(f"Dictionary 1: {dict1}")
print(f"Dictionary 2: {dict2}")
print(f"Dictionary 3: {dict3}")
print(f"Concatenated dictionary: {new_dict}")
