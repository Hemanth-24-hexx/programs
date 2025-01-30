numbers = [1, 2, 3, 4, 5]

def find_factors(n):
    factors = [i for i in range(1, n + 1) if n % i == 0]
    return factors

factors_dict = {num: find_factors(num) for num in numbers}
print(factors_dict)
