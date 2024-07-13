from collections import Counter

def combine_values(list_of_dicts):
    combined_counter = Counter()
    for d in list_of_dicts:
        combined_counter[d['item']] += d['amount']
    return dict(combined_counter)


sample_data = [{'item': 'item1', 'amount': 400}, 
               {'item': 'item2', 'amount': 300}, 
               {'item': 'item1', 'amount': 750}]


combined_dict = combine_values(sample_data)

print("Sample data:", sample_data)
print("Expected Output:")
print(combined_dict)
