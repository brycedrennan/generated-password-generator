# password generator 🔐🔑

**Cracking-proof keychains for cyber vaults**

A Python library for generating diverse types of secure and customizable passwords.

## Features
- Offers multiple password generation algorithms
- Customizable complexity and character sets
- Provides password strength evaluation

## Getting started
```bash
pip install password-generator
```
```python
from password_generator import generate_password, evaluate_strength

# Generate and evaluate different types of passwords
default_pwd = generate_password()
print(f"Default password: {default_pwd}")
print(f"Strength: {evaluate_strength(default_pwd)}")

custom_pwd = generate_password(length=20, include_symbols=True, include_numbers=True, include_uppercase=True)
print(f"Custom password: {custom_pwd}")
print(f"Strength: {evaluate_strength(custom_pwd)}")

passphrase = generate_password(algorithm="word-based", word_count=4, separator="-")
print(f"Passphrase: {passphrase}")
print(f"Strength: {evaluate_strength(passphrase)}")
```

## Project Structure

- `password_generator/__init__.py`
- `password_generator/generate.py`
- `password_generator/evaluate.py`
- `password_generator/algorithms.py`
- `password_generator/utils.py`
- `password_generator/constants.py`

## Changelog

## Development
 
 - Install pyenv
 - Git clone the project
 - Run `make init` to create the environment and install the dependencies
 - You can now run:
   - `make help` to see the available commands
   - `make test` to run the tests
   - `make lint` to run the linter
   - `make autoformat` to format the code
   - `make type-check` to run the type checker