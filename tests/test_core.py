
import hashlib
import os
import tempfile
import unittest

from forgeguard.core import (
    generate_password,
    password_strength,
    sha256_file,
    looks_like_email,
)


class ForgeGuardTests(unittest.TestCase):

    def test_password_length(self):
        password = generate_password(20)
        self.assertEqual(len(password), 20)

    def test_password_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(7)

    def test_password_strength(self):
        label, tips = password_strength("tiny")
        self.assertEqual(label, "Weak")
        self.assertTrue(tips)

    def test_empty_password(self):
        label, tips = password_strength("")
        self.assertEqual(label, "Very weak")
        self.assertTrue(tips)

    def test_file_hash(self):
        content = b"ForgeGuard test"

        with tempfile.NamedTemporaryFile(
            delete=False
        ) as file:
            file.write(content)
            path = file.name

        try:
            expected = hashlib.sha256(content).hexdigest()
            self.assertEqual(sha256_file(path), expected)
        finally:
            os.unlink(path)

    def test_email_validation(self):
        self.assertTrue(looks_like_email("dev@example.com"))
        self.assertFalse(looks_like_email("invalid-email"))
        self.assertFalse(looks_like_email("dev @example.com"))


if __name__ == "__main__":
    unittest.main()
          
