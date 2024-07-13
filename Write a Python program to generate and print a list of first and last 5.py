def generate_squares():
    squares = [i ** 2 for i in range(1, 31)]
    return squares[:5] + squares[-5:]

result = generate_squares()
print(f"First and last 5 elements of squares of numbers between 1 and 30: {result}")
