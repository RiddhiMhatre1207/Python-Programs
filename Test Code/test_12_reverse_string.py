import unittest
from _12_reverse_string import reverse_string

class TestReverseString(unittest.TestCase):

    def test_normal_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_palindrome(self):
        self.assertEqual(reverse_string("madam"), "madam")

    def test_with_spaces(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

if __name__ == "__main__":
    unittest.main()