def sort_dict_by_value(d, ascending=True):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=not ascending))


my_dict = {'a': 3, 'b': 1, 'c': 2, 'd': 4}


sorted_dict_ascending = sort_dict_by_value(my_dict, ascending=True)
print(f"Original dictionary: {my_dict}")
print(f"Dictionary sorted by value in ascending order: {sorted_dict_ascending}")


sorted_dict_descending = sort_dict_by_value(my_dict, ascending=False)
print(f"Dictionary sorted by value in descending order: {sorted_dict_descending}")
