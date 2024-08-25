import pytest

from password_generator import generate_password


def test_default_password():
    password = generate_password()
    assert len(password) == 12
    assert any(c.islower() for c in password)
    assert any(c.isupper() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)


def test_character_based_password():
    password = generate_password(length=20, include_symbols=False, include_numbers=True, include_uppercase=True)
    assert len(password) == 20
    assert any(c.islower() for c in password)
    assert any(c.isupper() for c in password)
    assert any(c.isdigit() for c in password)
    assert not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)


def test_word_based_password():
    password = generate_password(algorithm="word-based")
    assert len(password.split("-")) == 4


def test_word_based_password_custom():
    password = generate_password(algorithm="word-based", word_count=5, separator="_")
    assert len(password.split("_")) == 5


def test_invalid_algorithm():
    with pytest.raises(ValueError):
        generate_password(algorithm="invalid")
