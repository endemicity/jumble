import pytest

from ..logic.wordlist import get_words, get_letter_hashes


def test_default_words():
    assert get_words() == set(["a", "an", "cab", "bot", "boot", "zoo"])


def test_letter_hashes():
    default_words = set(["a", "bot", "boot", "cab"])
    letter_hashes = get_letter_hashes(default_words)

    assert "a" in letter_hashes
    assert "b" in letter_hashes
    assert "c" in letter_hashes
    assert letter_hashes["a"] == set(["a", "cab"])
    assert letter_hashes["b"] == set(["boot", "bot", "cab"])
    assert letter_hashes["c"] == set(["cab"])
