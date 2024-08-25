import pytest

from password_generator.algorithms import (
    create_character_set,
    generate_memorable_password,
    generate_pin,
    generate_pronounceable_password,
    select_random_words,
)


def test_create_character_set_all():
    assert (
        create_character_set(True, True, True)
        == "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    )


def test_create_character_set_lowercase_only():
    assert create_character_set(False, False, False) == "abcdefghijklmnopqrstuvwxyz"


def test_select_random_words():
    words = select_random_words(3)
    assert len(words) == 3
    assert all(isinstance(word, str) for word in words)


def test_generate_pin_default():
    pin = generate_pin()
    assert len(pin) == 4
    assert pin.isdigit()


def test_generate_pin_custom_length():
    pin = generate_pin(6)
    assert len(pin) == 6
    assert pin.isdigit()


def test_generate_pronounceable_password():
    password = generate_pronounceable_password()
    assert len(password) == 8
    assert password.isalpha()
    assert all(password[i] in "aeiou" if i % 2 else password[i] not in "aeiou" for i in range(len(password)))


def test_generate_memorable_password():
    password = generate_memorable_password()
    parts = password.split("-")
    assert len(parts) == 4
    assert all(part.isalpha() for part in parts[:3])
    assert parts[3].isdigit()
    assert len(parts[3]) == 2


def test_invalid_input():
    with pytest.raises(ValueError):
        generate_pin(0)
    with pytest.raises(ValueError):
        generate_memorable_password(0)
