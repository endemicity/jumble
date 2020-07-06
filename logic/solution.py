import re

from .exceptions import LettersValueError
from .wordlist import get_words, get_letter_hashes


def answers(letters, words_file="test"):
    letters = validate_letters(letters)
    num_letters = len(letters)
    if num_letters == 0:
        return []

    words = get_words(words_file)
    has_letter_hashes = get_letter_hashes(words)

    answers = set()
    for letter in letters:
        if letter in words:
            answers.add(letter)

    return list(answers)


def validate_letters(letters):
    num_letters = len(letters)
    if num_letters == 0:
        return letters

    letters = letters.lower()
    if not re.match("[a-z]+", letters):
        raise LettersValueError("Letters besides a-z in input")

    unique_letters = list(set(letters))
    num_unique_letters = len(unique_letters)
    if num_letters != num_unique_letters:
        raise LettersValueError("Duplicate letters in input")

    return unique_letters


if __name__ == "__MAIN__":
    print(answers("abc", words_file="wlist_match12"))
