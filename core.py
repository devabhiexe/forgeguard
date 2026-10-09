
"""Core utilities for ForgeGuard."""

import hashlib
import secrets
import string
from pathlib import Path

CHARACTERS = (
    string.ascii_letters
    + string.digits
    + "!@#$%^&*()-_=+[]{}?"
)


def generate_password(length: int = 16) -> str:
    """Generate a secure random password."""
    if not 8 <= length <= 128:
        raise ValueError("Length must be between 8 and 128.")

    return "".join(
        secrets.choice(CHARACTERS) for _ in range(length)
    )


def password_strength(password: str) -> tuple[str, list[str]]:
    """Give a simple password-strength estimate."""
    if not password:
        return "Very weak", ["Use a longer password."]

    tips = []
    categories = sum([
        any(c.islower() for c in password),
        any(c.isupper() for c in password),
        any(c.isdigit() for c in password),
        any(not c.isalnum() for c in password),
    ])

    if len(password) < 12:
        tips.append("Try using at least 12 characters.")

    if categories < 3:
        tips.append("Use a mix of character types.")

    if len(password) >= 16 and categories >= 3:
        label = "Strong"
    elif len(password) >= 12 and categories >= 2:
        label = "Moderate"
    else:
        label = "Weak"

    if not tips:
        tips.append("No obvious issues found by this basic check.")

    return label, tips


def sha256_file(path: str) -> str:
    """Calculate the SHA-256 hash of a file."""
    digest = hashlib.sha256()

    with Path(path).open("rb") as file:
        for chunk in iter(lambda: file.read(65536), b""):
            digest.update(chunk)

    return digest.hexdigest()


def looks_like_email(value: str) -> bool:
    """Perform a basic email-format check."""
    if not isinstance(value, str) or len(value) > 254:
        return False

    if value.count("@") != 1 or any(c.isspace() for c in value):
        return False

    local, domain = value.rsplit("@", 1)

    return (
        bool(local)
        and len(local) <= 64
        and "." in domain
        and not domain.startswith(".")
        and not domain.endswith(".")
        and all(domain.split("."))
                     )
