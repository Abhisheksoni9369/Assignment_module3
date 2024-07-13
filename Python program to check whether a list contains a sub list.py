def is_sublist(lst, sublist):
    n = len(sublist)
    return any((sublist == lst[i:i+n]) for i in range(len(lst) - n + 1))

main_list = [1, 2, 3, 4, 5, 6, 7, 8]
sub_list1 = [3, 4, 5]
sub_list2 = [5, 6, 9]

print(f"Does main_list contain sub_list1? {'Yes' if is_sublist(main_list, sub_list1) else 'No'}")
print(f"Does main_list contain sub_list2? {'Yes' if is_sublist(main_list, sub_list2) else 'No'}")
