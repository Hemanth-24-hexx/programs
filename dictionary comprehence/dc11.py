input_string = "hello world"

char_frequency = {char: input_string.count(char) for char in set(input_string)}
print(char_frequency)
