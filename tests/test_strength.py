from password_generator import evaluate_strength, generate_password


def test_weak_password():
    result = evaluate_strength("password123")
    assert result["score"] <= 1


def test_moderate_password():
    result = evaluate_strength("Tr0ub4dor&3")
    assert 1 < result["score"] <= 3


def test_strong_password():
    result = evaluate_strength("xT9$mK2#pL7@qR5")
    assert result["score"] >= 3


def test_empty_password():
    result = evaluate_strength("")
    assert result["score"] == 0
    assert result["crack_time_seconds"] == 0


def test_generated_password():
    password = generate_password()
    result = evaluate_strength(password)
    assert result["score"] >= 3  # Assuming generated passwords should be strong
