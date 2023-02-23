words = input("Enter the sentences: ")
words = words.split()

wordsReversed = list(reversed(words))
wordsReversed = " ".join(wordsReversed)

print("The reversed sentence: {0}".format(wordsReversed))