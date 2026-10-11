import unittest
from palindrome_string import is_palindrome

class TestPalindromeString(unittest.TestCase):

    def test_palindrome(self):
        self.assertTrue(is_palindrome("Hiii"))

    def test_another_palindrome(self):
        self.assertTrue(is_palindrome("level"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

if __name__ == "__main__":
    unittest.main()