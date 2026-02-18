# Your Name: Jorge
# Your Section:09

import Lab4
import unittest

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Task 1
    def test_last_element_1(self):
        input = [[1, 2], [3, 4], []]
        result = Lab4.last_element(input)
        expected = [2, 4]
        self.assertEqual(expected, result)

    def test_last_element_2(self):
        input = [[], [5.5], [1.1, 2.2]]
        result = Lab4.last_element(input)
        expected = [5.5, 2.2]
        self.assertEqual(expected, result)

    # Task 2
    def test_pass_fail_1(self):
        grades = [[90, 95], [60, 70]]
        result = Lab4.pass_fail(grades, 65)
        expected = ["pass", "fail"]
        self.assertEqual(expected, result)

    def test_pass_fail_2(self):
        grades = [[80, 85], [90, 100]]
        result = Lab4.pass_fail(grades, 75)
        expected = ["pass", "pass"]
        self.assertEqual(expected, result)

    # Task 3
    def test_search_value_1(self):
        result = Lab4.search_value([1, 2, 3], 2)
        self.assertEqual("Found", result)

    def test_search_value_2(self):
        result = Lab4.search_value(["a", "b", "c"], "z")
        self.assertEqual("Not Found", result)

    # Task 4
    def test_search_any_1(self):
        self.assertTrue(Lab4.search_any([10, 20, 30], 20))

    def test_search_any_2(self):
        self.assertFalse(Lab4.search_any([1, 2, 3], 5))

    # Task 5
    def test_reverse_value_1(self):
        result = Lab4.reverse_value([1, 2, 3])
        self.assertEqual([3, 2, 1], result)

    def test_reverse_value_2(self):
        result = Lab4.reverse_value("abc")
        self.assertEqual("cba", result)




if __name__ == '__main__':
    unittest.main()
