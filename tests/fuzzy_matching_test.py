import unittest
import search_engine.fuzzy_matching as fm


class TestFuzzyMatch(unittest.TestCase):

    def test_case1(self):
        result = fm.fuzzy_match_two_seq([1, 2, 3, 4, 5, 6, 7, 8], [10, 2, 4, 6, 7, 8], 3, 1)
        self.assertTrue(result)

    def test_case2(self):
        result = fm.fuzzy_match_two_seq([1, 2, 3, 4, 5, 6, 7, 8], [10, 2, 4, 6, 7, 8], 2, 1)
        self.assertFalse(result)

    def test_case3(self):
        result = fm.fuzzy_match_two_seq([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 4, 6, 7], 2, 1)
        self.assertFalse(result)

    def test_case4(self):
        result = fm.fuzzy_match_two_seq([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 4, 6, 7], 3, 1)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
