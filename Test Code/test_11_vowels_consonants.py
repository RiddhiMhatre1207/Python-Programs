import unittest

def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    for ch in text.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants


class TestVowelsConsonants(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(count_vowels_consonants("Hello World"), (3, 7))

    def test_all_vowels(self):
        self.assertEqual(count_vowels_consonants("aeiou"), (5, 0))

    def test_all_consonants(self):
        self.assertEqual(count_vowels_consonants("bcdf"), (0, 4))

    def test_empty_string(self):
        self.assertEqual(count_vowels_consonants(""), (0, 0))

    def test_numbers_and_spaces(self):
        self.assertEqual(count_vowels_consonants("abc 123"), (1, 2))


if __name__ == "__main__":
    unittest.main()