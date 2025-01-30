words = ['apple', 'banana', 'cherry']

def count_vowels(word):
    vowels = 'aeiou'
    return sum(1 for letter in word if letter in vowels)

vowel_counts = {word: count_vowels(word) for word in words}
print(vowel_counts)
