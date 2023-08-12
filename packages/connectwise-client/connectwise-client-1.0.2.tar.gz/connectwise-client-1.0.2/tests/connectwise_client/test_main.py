"""Test the main module."""

# Standard libs
import unittest

# Custom libs
from connectwise_client.main import hello


class TestMain(unittest.TestCase):
    """Testing class for the main."""

    def test_hello(self) -> None:
        """Test hello function."""
        result = hello("unused")
        self.assertEqual(result, "hello unused")
