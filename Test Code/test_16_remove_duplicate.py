import unittest

def remove_duplicates(numbers):
    return list(dict.fromkeys(numbers))


class TestRemoveDuplicates(unittest.TestCase):

    def test_normal_list(self):
        self.assertEqual(
            remove_duplicates([1, 2, 2, 3, 1]),
            [1, 2, 3]
        )

    def test_no_duplicates(self):
        self.assertEqual(
            remove_duplicates([1, 2, 3]),
            [1, 2, 3]
        )

    def test_all_duplicates(self):
        self.assertEqual(
            remove_duplicates([5, 5, 5]),
            [5]
        )

    def test_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_single_element(self):
        self.assertEqual(remove_duplicates([10]), [10])

    def test_negative_numbers(self):
        self.assertEqual(
            remove_duplicates([-1, -2, -1, -3, -2]),
            [-1, -2, -3]
        )


if __name__ == "__main__":
    unittest.main()
