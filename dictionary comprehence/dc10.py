words = ['apple', 'banana', 'cherry', 'date']

long_words = {word: len(word) for word in words if len(word) > 5}
print(long_words)
