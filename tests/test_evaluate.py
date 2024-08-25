"""Tests for the password strength evaluation functionality."""

from password_generator import evaluate_strength


def test_weak_password():
    result = evaluate_strength("password123")
    assert result["score"] <= 1
    assert result["crack_time_seconds"] < 3600  # Less than 1 hour


def test_moderate_password():
    result = evaluate_strength("Tr0ub4dor&3")
    assert 1 < result["score"] <= 3
    assert 3600 <= result["crack_time_seconds"] < 31536000  # Between 1 hour and 1 year


def test_strong_password():
    result = evaluate_strength("xT9$mK2#pL7@qR5")
    assert result["score"] >= 3
    assert result["crack_time_seconds"] > 31536000  # More than 1 year


def test_empty_password():
    result = evaluate_strength("")
    assert result["score"] == 0
    assert result["crack_time_seconds"] == 0
