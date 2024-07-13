def find_max_min(numbers):
    if not numbers:
        return None, None
    
    max_number = max(numbers)
    min_number = min(numbers)
    
    return max_number, min_number

decimal_numbers = [3.14, 2.718, 1.618, 0.577, 4.669]
max_num, min_num = find_max_min(decimal_numbers)

print(f"Maximum number: {max_num}")
print(f"Minimum number: {min_num}")
