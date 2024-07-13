def list_statistics(lst):
    if not lst:
        return None, None, 0  
    
    largest_num = max(lst)
    smallest_num = min(lst)
    sum_of_numbers = sum(lst)
    
    return largest_num, smallest_num, sum_of_numbers

list1 = [2, 33, 222, 14, 25]
largest, smallest, total = list_statistics(list1)
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
print(f"Sum of all numbers: {total}")
