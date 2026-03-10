from group import group_of_3
import unittest


class TestCases(unittest.TestCase):
        def test_group_of_3(self):
            list1 = [1,2,3,4,5,6,7,8,9]
            expected =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            result = group_of_3(list1)
            self.assertEqual(result, expected)

        def test_group_of_3_1(self):
            list2 = [1,2,3,4,5,6,7,8,9,10,11,12]
            expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
            result=group_of_3(list2)
            self.assertEqual(result, expected)