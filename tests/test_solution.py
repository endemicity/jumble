import pytest

from ..solution import answers


def test_no_letters():
    assert answers("") == []


def test_valid_one_letter():
    assert answers("a") == ["a"]


def test_invalid_one_letter():
    assert answers("b") == []


def test_duplicate_letters():
    with pytest.raises(ValueError):
        answers("aa")


def test_non_alpha():
    with pytest.raises(ValueError):
        answers("-")


def test_valid_two_letters():
    assert answers("ab") == ["a"]


def test_invalid_two_letters():
    assert answers("bc") == []
