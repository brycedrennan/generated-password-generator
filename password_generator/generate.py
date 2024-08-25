import secrets
import string

from password_generator.constants import WORD_LIST


def generate_password(
    length: int = 12,
    include_symbols: bool = True,
    include_numbers: bool = True,
    include_uppercase: bool = True,
    algorithm: str = "character-based",
    word_count: int | None = None,
    separator: str = "-",
) -> str:
    """
    Generate a secure, customizable password.

    Args:
        length: Length of the password for character-based algorithm.
        include_symbols: Whether to include symbols in character-based passwords.
        include_numbers: Whether to include numbers in character-based passwords.
        include_uppercase: Whether to include uppercase letters in character-based passwords.
        algorithm: Either "character-based" or "word-based".
        word_count: Number of words for word-based algorithm.
        separator: Separator for word-based passwords.

    Returns:
        A generated password string.

    Raises:
        ValueError: If invalid algorithm is specified or invalid input parameters.
    """
    if algorithm == "character-based":
        return _generate_character_based(length, include_symbols, include_numbers, include_uppercase)
    elif algorithm == "word-based":
        return _generate_word_based(word_count or 4, separator)
    else:
        raise ValueError("Invalid algorithm specified")


def _generate_character_based(length, include_symbols, include_numbers, include_uppercase):
    if length <= 0:
        raise ValueError("Length must be a positive integer")
    chars = string.ascii_lowercase
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_numbers:
        chars += string.digits
    if include_symbols:
        chars += string.punctuation
    return "".join(secrets.choice(chars) for _ in range(length))


def _generate_word_based(word_count, separator):
    if word_count <= 0:
        raise ValueError("Word count must be a positive integer")
    return separator.join(secrets.choice(WORD_LIST) for _ in range(word_count))
