
"""Command-line interface for ForgeGuard."""

import argparse
import getpass
import sys

from .core import (
    generate_password,
    password_strength,
    sha256_file,
    looks_like_email,
)


def main():
    parser = argparse.ArgumentParser(
        description="ForgeGuard Python security utilities"
    )
    commands = parser.add_subparsers(
        dest="command", required=True
    )

    password_cmd = commands.add_parser("password")
    password_cmd.add_argument("--length", type=int, default=16)

    commands.add_parser("strength")

    hash_cmd = commands.add_parser("hash")
    hash_cmd.add_argument("path")

    email_cmd = commands.add_parser("validate-email")
    email_cmd.add_argument("value")

    args = parser.parse_args()

    try:
        if args.command == "password":
            print(generate_password(args.length))

        elif args.command == "strength":
            password = getpass.getpass("Password (hidden): ")
            label, tips = password_strength(password)
            print(f"Strength: {label}")
            for tip in tips:
                print(f"- {tip}")

        elif args.command == "hash":
            print(sha256_file(args.path))

        elif args.command == "validate-email":
            valid = looks_like_email(args.value)
            print("Looks valid." if valid else "Invalid email format.")
            return 0 if valid else 1

    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
          
