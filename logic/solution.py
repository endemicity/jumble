import re

from .exceptions import LettersValueError
from .wordlist import get_words, get_letter_hashes


def answers(letters, words_file="test"):
    letters = validate_letters(letters)
    num_letters = len(letters)
    if num_letters == 0:
        return []

    words = get_words(words_file)
    letter_hashes = get_letter_hashes(words)

    sets_to_intersect = []
    for letter in letters:
        sets_to_intersect.append(letter_hashes[letter])

    first_set = sets_to_intersect.pop()
    possible_words = list(first_set.intersection(*sets_to_intersect))

    answers = []
    for word in possible_words:
        word_letters = list(set(word))
        word_letters.sort()
        if letters == word_letters:
            answers.append(word)

    return answers


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

    unique_letters.sort()
    return unique_letters
