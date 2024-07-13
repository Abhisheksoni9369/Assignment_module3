from collections import Counter

def combine_dicts(dict1, dict2):
    
    counter1 = Counter(dict1)
    counter2 = Counter(dict2)

    
    combined_counter = counter1 + counter2

    return dict(combined_counter)  

dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}

combined_dict = combine_dicts(dict1, dict2)

print(f"Dictionary 1: {dict1}")
print(f"Dictionary 2: {dict2}")
print(f"Combined Dictionary with sum of values for common keys: {combined_dict}")
