def sum_of_divisors(n):
    if n <= 0:
        return 0
    
    sum_divisors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum_divisors += i
    
    return sum_divisors

number = 28

sum_divisors = sum_of_divisors(number)
print(f"The sum of all divisors of {number} is: {sum_divisors}")
