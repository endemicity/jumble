import pytest

from ..logic.solution import solve_pangram


def test_no_letters():
    assert solve_pangram("") == []


def test_valid_one_letter():
    assert solve_pangram("a") == ["a"]


def test_invalid_one_letter():
    assert solve_pangram("b") == []


def test_duplicate_letters():
    with pytest.raises(ValueError):
        solve_pangram("aa")


def test_non_alpha():
    with pytest.raises(ValueError):
        solve_pangram("-")


def test_valid_two_letters():
    assert solve_pangram("an") == ["an"]


def test_invalid_two_letters():
    assert solve_pangram("bc") == []


def test_valid_three_letters():
    assert solve_pangram("abc") == ["cab"]


def test_repeated_three_letters():
    assert solve_pangram("bot") == ["boot", "bot"]

