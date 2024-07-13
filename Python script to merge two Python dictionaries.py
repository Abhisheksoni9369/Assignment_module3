def merge_dictionaries_update(dict1, dict2):
    merged_dict = dict1.copy()  
    merged_dict.update(dict2)   
    return merged_dict

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = merge_dictionaries_update(dict1, dict2)


print(f"Dictionary 1: {dict1}")
print(f"Dictionary 2: {dict2}")
print(f"Merged Dictionary: {merged_dict}\n")
