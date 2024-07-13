def is_perfect_number(num):
    if num <= 0:
        return False
    
    
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    

    return sum_divisors == num

number = 28

if is_perfect_number(number):
    print(f"{number} is a perfect number")
else:
    print(f"{number} is not a perfect number")
