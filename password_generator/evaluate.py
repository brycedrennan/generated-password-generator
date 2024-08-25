import zxcvbn


def evaluate_strength(password: str) -> dict[str, int]:
    """
    Evaluate the strength of a given password.

    Args:
        password: The password to evaluate.

    Returns:
        A dictionary containing the score and estimated crack time.
        Score ranges from 0 (very weak) to 4 (very strong).
    """
    result = zxcvbn.zxcvbn(password)
    return {
        "score": result["score"],
        "crack_time_seconds": result["crack_times_seconds"]["offline_slow_hashing_1e4_per_second"],
    }
