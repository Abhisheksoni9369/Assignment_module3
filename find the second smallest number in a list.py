def second_smallest(lst):
    if len(lst) < 2:
        return None  
    
    smallest = float('inf')
    second_smallest = float('inf')
    
    for num in lst:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    
    return second_smallest


my_list = [5, 2, 3, 1, 4]
result = second_smallest(my_list)
print(f"The second smallest number in the list {my_list} is: {result}")
