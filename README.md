
# ForgeGuard 🛡️

ForgeGuard is a lightweight, beginner-friendly Python toolkit offering
simple password utilities, file hashing, and basic input validation.

## Features

- Secure random password generation using Python's `secrets` module
- Basic password-strength estimation
- SHA-256 file hashing
- Basic email-format validation
- Unit tests using Python's standard library

## Requirements

- Python 3.10+
- No third-party dependencies

## Usage

Generate a password:

```bash
python -m forgeguard password --length 20
```

Check password strength:

```bash
python -m forgeguard strength
```

Calculate a file's SHA-256 hash:

```bash
python -m forgeguard hash example.txt
```

Validate an email:

```bash
python -m forgeguard validate-email dev@example.com
```

## Run Tests

From the repository root:

```bash
python -m unittest discover -s tests -v
```

## Security Notes

ForgeGuard is an educational utility, not a complete security
auditing tool. Password-strength results are heuristic estimates.
Email validation does not confirm that an address exists.

## Contributing

Contributions are welcome! Please include tests for bug fixes
and new features.

## License

This project is released under the MIT License.
