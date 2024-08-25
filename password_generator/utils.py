import math
import string


def calculate_entropy(password: str) -> float:
    """Calculate the entropy of a given password."""
    if not password:
        return 0.0
    char_set = set(password)
    return len(password) * math.log2(len(char_set))


def get_character_set(lowercase: bool = True, uppercase: bool = True, digits: bool = True, symbols: bool = True) -> str:
    """Generate a character set based on specified criteria."""
    chars = ""
    if lowercase:
        chars += string.ascii_lowercase
    if uppercase:
        chars += string.ascii_uppercase
    if digits:
        chars += string.digits
    if symbols:
        chars += string.punctuation
    return chars


def validate_password_complexity(password: str, required_sets: set[str]) -> bool:
    """
    Validate that a password contains characters from all required sets.

    Args:
        password: The password to validate.
        required_sets: A set of strings, each representing a required character set
                       (e.g., {"lowercase", "uppercase", "digits", "symbols"}).

    Returns:
        True if the password contains characters from all required sets, False otherwise.
    """
    char_sets = {
        "lowercase": set(string.ascii_lowercase),
        "uppercase": set(string.ascii_uppercase),
        "digits": set(string.digits),
        "symbols": set(string.punctuation),
    }

    return all(set(password) & char_sets[req_set] for req_set in required_sets)
