def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers_prime_status = {i: is_prime(i) for i in range(1, 11)}
print(numbers_prime_status)
