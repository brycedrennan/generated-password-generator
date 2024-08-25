import pytest

from password_generator import generate_password


def test_default_character_based_password():
    password = generate_password()
    assert len(password) == 12
    assert any(c.islower() for c in password)
    assert any(c.isupper() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)


def test_custom_character_based_password():
    password = generate_password(length=20, include_symbols=False, include_numbers=True, include_uppercase=True)
    assert len(password) == 20
    assert any(c.islower() for c in password)
    assert any(c.isupper() for c in password)
    assert any(c.isdigit() for c in password)
    assert not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)


def test_lowercase_only_password():
    password = generate_password(include_symbols=False, include_numbers=False, include_uppercase=False)
    assert password.islower()


def test_long_password():
    password = generate_password(length=128)
    assert len(password) == 128


def test_invalid_length():
    with pytest.raises(ValueError):
        generate_password(length=0)


def test_no_character_types():
    with pytest.raises(ValueError):
        generate_password(
            include_symbols=False, include_numbers=False, include_uppercase=False, include_lowercase=False
        )
