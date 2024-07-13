def in_range(num, start, end):
    return start <= num <= end


number = 15
lower_bound = 10
upper_bound = 20


if in_range(number, lower_bound, upper_bound):
    print(f"{number} is in the range [{lower_bound}, {upper_bound}]")
else:
    print(f"{number} is not in the range [{lower_bound}, {upper_bound}]")
