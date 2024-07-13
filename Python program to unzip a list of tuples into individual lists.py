def unzip_tuples(tuples_list):
    return list(zip(*tuples_list))

my_list_of_tuples = [(1, 2), (3, 4), (5, 6)]
unzipped_lists = unzip_tuples(my_list_of_tuples)
print(f"Original list of tuples: {my_list_of_tuples}")
print(f"Unzipped lists: {unzipped_lists}")

unzipped_lists = [list(tup) for tup in unzipped_lists]
print(f"Unzipped lists as lists: {unzipped_lists}")
