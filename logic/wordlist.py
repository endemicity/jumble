import re

from pathlib import Path
from string import ascii_lowercase


def get_words(words_file="test"):
    words_path = Path(__file__).parent.parent.absolute()
    words = set()
    raw_words = []
    with open("{}/words/{}.txt".format(words_path, words_file)) as f:
        raw_words = f.readlines()

    for word in raw_words:
        # if not re.match('[a-z]+', word):
        #    continue
        word = word.strip()
        word = word.lower()
        words.add(word)

    return words


def get_letter_hashes(words):
    hashes = {}
    for letter in ascii_lowercase:
        hashes[letter] = set()

    for word in words:
        for letter in ascii_lowercase:
            if letter in word:
                hashes[letter].add(word)

    return hashes
