numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

multiples_of_3_squares = {num: num**2 for num in numbers if num % 3 == 0}
print(multiples_of_3_squares)
