import unittest

def second_largest(numbers):
    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        return None

    unique_numbers.sort(reverse=True)
    return unique_numbers[1]


class TestSecondLargest(unittest.TestCase):

    def test_normal_list(self):
        self.assertEqual(second_largest([10, 20, 50, 40, 30]), 40)

    def test_duplicate_numbers(self):
        self.assertEqual(second_largest([10, 10, 5, 3]), 5)

    def test_negative_numbers(self):
        self.assertEqual(second_largest([-10, -5, -20]), -10)

    def test_two_numbers(self):
        self.assertEqual(second_largest([10, 20]), 10)

    def test_all_same_numbers(self):
        self.assertIsNone(second_largest([5, 5, 5]))

    def test_empty_list(self):
        self.assertIsNone(second_largest([]))

    def test_single_number(self):
        self.assertIsNone(second_largest([10]))


if __name__ == "__main__":
    unittest.main()

