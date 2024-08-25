"""A Python library for generating diverse types of secure and customizable passwords."""

from password_generator.evaluate import evaluate_strength
from password_generator.generate import generate_password
from password_generator.version import __version__

__all__ = ["generate_password", "evaluate_strength"]
