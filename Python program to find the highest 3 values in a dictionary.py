def highest_3_values(d):
    
    sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)
    highest_values = sorted_items[:3]

    return highest_values

my_dict = {'a': 100, 'b': 200, 'c': 50, 'd': 300, 'e': 150}

top_3_values = highest_3_values(my_dict)

print("Dictionary:", my_dict)
print("Highest 3 values:", top_3_values)
