#Name:
#Section:

import data
from project1 import *
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count1(self):
        str1 = 'This is a test for vowels'
        expected = 7
        self.assertEqual(vowel_count(str1), expected)

    def test_vowel_count2(self):
        str1 = "AEIOU"
        expected = 5
        self.assertEqual(vowel_count(str1), expected)

    def test_vowel_count(self):
        str1 = "Hi there"
        expected = 3
        self.assertEqual(vowel_count(str1), expected)

    # Part 2
    def test_long_lists1(self):
        lists = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
        expected = [[3, 4, 5], [6, 7, 8, 9]]
        self.assertEqual(long_lists(lists), expected)

    def test_long_lists2(self):
        lists = [[1], [2, 3]]
        expected = []
        self.assertEqual(long_lists(lists), expected)
    
    def test_short_lists3(self):
        lists = [[1, 2, 3], [], [4, 5], [6, 7, 8, 9]]
        expected = [[1, 2, 3], [6, 7, 8, 9]]
        self.assertEqual(long_lists(lists), expected)

    # Part 3
    def test_decending_pairs1(self):
        lst = [[12,2,3],[10,2],[-9,0,9,78],[15,6],[1,2]]
        expected = [[12, 2, 3], [10, 2], [-9, 0, 9, 78], [15, 6], [2, 1]]
        self.assertEqual(decending_pairs(lst), expected)

    def test_decending_pairs2(self):
        lst = [[12, 2, 3], [10, 2, 0], [-9, 0, 9, 78], [1, 5, 6]]
        expected = [[12, 2, 3], [10, 2, 0], [-9, 0, 9, 78], [1, 5, 6]]
        self.assertEqual(decending_pairs(lst), expected)
    
    def test_decending_pairs3(self):
        lst = [[9, 3], [5, 5], [1, 2, 3]]
        expected = [[9, 3], [5, 5], [1, 2, 3]]
        self.assertEqual(decending_pairs(lst), expected)

    # Part 4
    def test_Price_add1(self):
        p1 = data.Price(2, 50)
        p2 = data.Price(3, 25)
        expected = data.Price(5, 75)
        self.assertEqual(add_prices(p1, p2), expected)
    
    def test_Price_add2(self):
        p1 = data.Price(1, 75)
        p2 = data.Price(2, 50)
        expected = data.Price(4, 25)
        self.assertEqual(add_prices(p1, p2), expected)

    # Part 5
    def test_perimeter1(self):
        rect = data.Rectangle(data.Point(1, 1),data.Point(2, 0))
        expected = 4
        self.assertEqual(rectangle_perimeter(rect), expected)

    def test_perimeter2(self):
        rect = data.Rectangle(data.Point(0, 4), data.Point(4, 0))
        expected = 16
        self.assertEqual(rectangle_perimeter(rect), expected)
    
    # Part 6

    def test_negative_quadrant_1(self):
        points = [data.Point(2, -1), data.Point(-1, -7), data.Point(0,5), data.Point(-9,-3)]
        expected = [data.Point(-1, -7), data.Point(-9, -3)]
        self.assertEqual(are_in_negative_quadrant(points), expected)

    def test_negative_quadrant_2(self):
        points = [data.Point(1, 1), data.Point(-1, 2)]
        expected = []
        self.assertEqual(are_in_negative_quadrant(points), expected)
        


    # Part 7
    def test_circle_bound_1(self):
        rec = data.Rectangle(data.Point(-5, 20), data.Point(12, 10))
        expected_center = data.Point(3.5, 15)
        self.assertEqual(circle_bound(rec).center, expected_center)

    def test_circle_bound_2(self):
        rec = data.Rectangle(data.Point(-5, 20), data.Point(12, 10))
        expected_radius = ((-5 - 3.5) ** 2 + (20 - 15) ** 2) ** 0.5
        self.assertAlmostEqual(circle_bound(rec).radius, expected_radius)
        
    # Part 8
    def test_higher_than_average1(self):
        emps = [
            data.Employee("Sam", 3000.0),
            data.Employee("Tom", 5000.0),
            data.Employee("Mary", 4000.0)
        ]
        expected = ["Tom"]
        self.assertEqual(higher_than_average(emps), expected)

    def test_higher_than_average2(self):
        emps = [
            data.Employee("Sam", 4000.0),
            data.Employee("Tom", 4000.0),
            data.Employee("Mary", 4000.0)
        ]
        expected = []
        self.assertEqual(higher_than_average(emps), expected)

    def test_higher_than_average(self):
        emps = []
        expected = []
        self.assertEqual(higher_than_average(emps), expected)



if __name__ == '__main__':
    unittest.main()
