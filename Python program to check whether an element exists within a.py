def element_exists_in_tuple(tup, element):
    return element in tup

my_tuple = (1, 2, 3, 4, 5)
element_to_check = 3

if element_exists_in_tuple(my_tuple, element_to_check):
    print(f"Element {element_to_check} exists in the tuple {my_tuple}")
else:
    print(f"Element {element_to_check} does not exist in the tuple {my_tuple}")
