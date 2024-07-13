def count_special_strings(strings):
    count = 0
    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

strings_list = ['abc', 'xyz', 'aba', '1221', 'ab']
result = count_special_strings(strings_list)
print(f"Number of strings with length 2: {result}")
