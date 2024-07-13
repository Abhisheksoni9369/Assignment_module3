def tuple_to_string(tup):
    return ''.join(str(item) for item in tup)

my_tuple = ('Hello', ' ', 'world', '!')
result_string = tuple_to_string(my_tuple)
print(f"Tuple: {my_tuple}")
print(f"Converted string: {result_string}")
