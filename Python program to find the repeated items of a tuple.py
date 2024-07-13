def find_repeated_items(tup):
    from collections import Counter
    item_counts = Counter(tup)
    repeated_items = [item for item, count in item_counts.items() if count > 1]
    return repeated_items


my_tuple = (1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 2)
repeated_items = find_repeated_items(my_tuple)
print(f"Original tuple: {my_tuple}")
print(f"Repeated items: {repeated_items}")
