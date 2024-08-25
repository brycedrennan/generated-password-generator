import pytest

from password_generator import generate_password
from password_generator.constants import WORD_LIST


def test_default_word_based_password():
    password = generate_password(algorithm="word-based")
    words = password.split("-")
    assert len(words) == 4
    assert all(word in WORD_LIST for word in words)


def test_custom_word_based_password():
    password = generate_password(algorithm="word-based", word_count=5, separator="_")
    words = password.split("_")
    assert len(words) == 5
    assert all(word in WORD_LIST for word in words)


def test_minimum_word_count():
    password = generate_password(algorithm="word-based", word_count=1)
    assert password in WORD_LIST


def test_invalid_word_count():
    with pytest.raises(ValueError):
        generate_password(algorithm="word-based", word_count=0)
