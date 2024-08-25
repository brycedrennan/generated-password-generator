import pytest

from password_generator import evaluate_strength, generate_password


@pytest.fixture()
def weak_password():
    return "password123"


@pytest.fixture()
def strong_password():
    return "xT9$mK2#pL7@qR5"


def test_generate_password_default():
    password = generate_password()
    assert len(password) == 12
    assert any(c.islower() for c in password)
    assert any(c.isupper() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)


def test_generate_password_custom():
    password = generate_password(length=20, include_symbols=False, include_numbers=True, include_uppercase=True)
    assert len(password) == 20
    assert any(c.islower() for c in password)
    assert any(c.isupper() for c in password)
    assert any(c.isdigit() for c in password)
    assert not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)


def test_generate_password_word_based():
    password = generate_password(algorithm="word-based", word_count=5, separator="_")
    assert len(password.split("_")) == 5


def test_generate_password_invalid_algorithm():
    with pytest.raises(ValueError):
        generate_password(algorithm="invalid")


def test_evaluate_strength(weak_password, strong_password):
    weak_result = evaluate_strength(weak_password)
    strong_result = evaluate_strength(strong_password)

    assert weak_result["score"] < strong_result["score"]
    assert weak_result["crack_time_seconds"] < strong_result["crack_time_seconds"]


def test_evaluate_strength_empty_password():
    result = evaluate_strength("")
    assert result["score"] == 0
    assert result["crack_time_seconds"] == 0
