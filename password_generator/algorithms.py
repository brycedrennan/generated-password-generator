import secrets
import string

from password_generator.constants import WORD_LIST


def create_character_set(include_uppercase: bool, include_numbers: bool, include_symbols: bool) -> str:
    chars = string.ascii_lowercase
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_numbers:
        chars += string.digits
    if include_symbols:
        chars += string.punctuation
    return chars


def select_random_words(count: int) -> list[str]:
    return [secrets.choice(WORD_LIST) for _ in range(count)]


def generate_pin(length: int = 4) -> str:
    return "".join(secrets.choice(string.digits) for _ in range(length))


def generate_pronounceable_password(length: int = 8) -> str:
    vowels = "aeiou"
    consonants = "".join(set(string.ascii_lowercase) - set(vowels))
    password = ""
    for i in range(length):
        if i % 2 == 0:
            password += secrets.choice(consonants)
        else:
            password += secrets.choice(vowels)
    return password


def generate_memorable_password(word_count: int = 3, num_digits: int = 2) -> str:
    words = select_random_words(word_count)
    digits = "".join(secrets.choice(string.digits) for _ in range(num_digits))
    return f"{'-'.join(words)}-{digits}"
