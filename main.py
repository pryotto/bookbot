book = "books/frankenstein.txt"

with open(book) as f:
    filecontents = f.read()

words = filecontents.split()
words = [c.lower() for c in words]
letters = dict()
for word in words:
    for letter in word:
        if not letter.isalpha(): continue
        if not letter in letters.keys(): letters[letter] = 0
        letters[letter] += 1

sorted_letters = list(letters.keys())
sorted_letters.sort()


def report(sorted_letters: list, letters: dict):
    print("--- begin report of {book} ---")
    print(f"{len(words)} words found in the document\n")
    for letter in sorted_letters:
        print(f"The '{letter}' character was found {letters[letter]} times")
    print("--- End of Report ---")

report(sorted_letters, letters)