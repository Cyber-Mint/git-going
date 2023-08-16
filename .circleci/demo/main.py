import unittest


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        result = sum([1, 2, 3])
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
