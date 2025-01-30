sentence = input("Enter String: ")
words = sentence.split()  # Split the sentence into words
word_lengths = {word: len(word) for word in words}
print(word_lengths)
