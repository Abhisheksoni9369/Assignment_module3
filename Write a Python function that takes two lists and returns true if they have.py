def have_common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
list3 = [10, 11, 12]

print(f"Do list1 and list2 have a common member? {'Yes' if have_common_member(list1, list2) else 'No'}")
print(f"Do list1 and list3 have a common member? {'Yes' if have_common_member(list1, list3) else 'No'}")
