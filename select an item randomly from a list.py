import random

def select_random_item(lst):
    return random.choice(lst)

my_list = [1, 2, 3, 4, 5]
random_item = select_random_item(my_list)
print(f"Randomly selected item from the list: {random_item}")
