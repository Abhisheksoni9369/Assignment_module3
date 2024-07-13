def count_chars(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


sample_string = 'w3resource'


char_dict = count_chars(sample_string)


print("Sample string:", sample_string)
print("Expected output:")
print(char_dict)
