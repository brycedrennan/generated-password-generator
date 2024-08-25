from password_generator.utils import calculate_entropy, get_character_set, validate_password_complexity


def test_calculate_entropy():
    assert calculate_entropy("") == 0.0
    assert calculate_entropy("a") > 0.0
    assert calculate_entropy("abcdefg") > calculate_entropy("aaaaaaa")
    assert calculate_entropy("P@ssw0rd!") > calculate_entropy("abcdefgh")


def test_get_character_set():
    assert get_character_set(lowercase=True, uppercase=False, digits=False, symbols=False).islower()
    assert get_character_set(lowercase=False, uppercase=True, digits=False, symbols=False).isupper()
    assert get_character_set(lowercase=False, uppercase=False, digits=True, symbols=False).isdigit()
    assert all(
        c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        for c in get_character_set(lowercase=False, uppercase=False, digits=False, symbols=True)
    )
    full_set = get_character_set(lowercase=True, uppercase=True, digits=True, symbols=True)
    assert any(c.islower() for c in full_set)
    assert any(c.isupper() for c in full_set)
    assert any(c.isdigit() for c in full_set)
    assert any(c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~" for c in full_set)


def test_validate_password_complexity():
    assert validate_password_complexity("Abcd123!", {"lowercase", "uppercase", "digits", "symbols"})
    assert not validate_password_complexity("abcd123!", {"lowercase", "uppercase", "digits", "symbols"})
    assert validate_password_complexity("abcd", {"lowercase"})
    assert not validate_password_complexity("ABCD", {"lowercase"})
    assert validate_password_complexity("AnyPassword", set())
