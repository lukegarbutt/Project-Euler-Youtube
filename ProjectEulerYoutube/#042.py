# Coded Triangle Numbers
import string
import csv
import math


def main():
    letter_to_number_dict = dict(zip(string.ascii_uppercase, [ord(c) % 32 for c in string.ascii_uppercase]))
    with open('#042_words.txt', 'r') as f:
        reader = csv.reader(f)
        words = list(reader)[0]
    total = 0
    for word in words:
        score = 0
        for letter in word:
            score += letter_to_number_dict[letter]
        if is_square(8*score+1):
            total += 1
    print(total)


def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        return True
    else:
        return False


main()


