def remove_duplicates(lst):
    return list(set(lst))

# Example usage
list1 = [1, 2, 3, 4, 5, 2, 3, 1]
unique_list = remove_duplicates(list1)
print(f"List after removing duplicates: {unique_list}")
