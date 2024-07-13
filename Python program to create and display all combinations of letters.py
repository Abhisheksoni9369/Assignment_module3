from itertools import product

def combinations_from_dict(d):
    
    lists = list(d.values())
    
    
    combinations = list(product(*lists))
    
    
    result = [''.join(comb) for comb in combinations]
    
    return result


sample_data = {'1': ['a', 'b'], '2': ['c', 'd']}

result = combinations_from_dict(sample_data)

print("Sample data:", sample_data)
print("Expected Output:")
print(' '.join(result))
