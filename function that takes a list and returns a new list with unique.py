def get_unique_elements(lst):
    unique_elements = []
    seen = set()
    for item in lst:
        if item not in seen:
            unique_elements.append(item)
            seen.add(item)
    return unique_elements

original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = get_unique_elements(original_list)
print(f"Original list: {original_list}")
print(f"Unique elements list: {unique_list}")
