# Name:
# Section:
#########################################################
import data
import Lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
	# Task 1
	def test_x_coord(self):
		points = [data.Point(1,2), data.Point(3,4), data.Point(5,6)]
		expected = [1,3,5]
		self.assertEqual(Lab5.x_coord(points), expected)

	def test_x_coord2(self):
		points = [data.Point(1.2,2), data.Point(-3.2,4), data.Point(92,6)]
		expected = [1.2,-3.2,92]
		self.assertEqual(Lab5.x_coord(points), expected)
	# Task 2
	def test_are_in_positive_quadrant(self):
		points = [data.Point(1,2), data.Point(-3,-4), data.Point(-5,6)]
		expected = [(1,2)]

	def test_are_in_positive_quadrant2(self):
		points = [data.Point(1,2), data.Point(3,4), data.Point(5,6)]
		expected = [(1,2),(3,4),(5,6)]
   	# Task 3
	def test_eucladian_distance(self):
		p1 = data.Point(1,2)
		p2 = data.Point(3,4)
		expected = 8

	def test_eucladian_distance2(self):
		p1 = data.Point(1,2)
		p2 = data.Point(4,4)
		expected = 13

	# Task 4
	def test_manhattan_distance(self):
		p1 = data.Point(1,2)
		p2 = data.Point(3,4)
		expected = 4

	def test_manhattan_distance2(self):
		p1 = data.Point(1,2)
		p2 = data.Point(4,4)
		expected = 5
	# Task 5
	def test_distance_all(self):
		points = [data.Point(0,0), data.Point(3,4) , data.Point(6,8)]
		expected = [0.0,5.0,10.0]
		self.assertEqual(Lab5.distance_all(points), expected)

	def test_distance_all2(self):
		points = [data.Point(0,5), data.Point(3,4)]
		expected = [5.0,5.0]
		self.assertEqual(Lab5.distance_all(points), expected)
	# Task 6
    #    Part 1 tests should be in data_tests.py.

    # Task 7
    #    Part 2 tests should be in data_tests.py.


    # Task 8 
	def test_time_add(self):
		t1 = data.Time(1, 20, 30)
		t2 = data.Time(2, 15, 10)
		expected = data.Time(3, 35, 40)
		self.assertEqual(Lab5.time_add(t1, t2), expected)

	def test_time_add2(self):
		t1 = data.Time(1, 59, 50)
		t2 = data.Time(0, 0, 15)
		expected = data.Time(2, 0, 5)
		self.assertEqual(Lab5.time_add(t1, t2), expected)

    # Task 9
	def test_is_descending(self):
		values = [9.0, 5.0, 1.0]
		expected = True
		self.assertEqual(Lab5.is_descending(values), expected)

	def test_is_descending2(self):
		values = [5.0, 3.0, 3.0]
		expected = False
		self.assertEqual(Lab5.is_descending(values), expected)


    # Task 10
	def test_largest_between(self):
		values = [4, 9, 2, 11, 7]
		expected = 3
		self.assertEqual(Lab5.largest_between(values, 1, 3), expected)

	def test_largest_between2(self):
		values = [4, 9, 2, 11, 7]
		expected = 3
		self.assertEqual(Lab5.largest_between(values, -5, 10), expected)
    # Task 11
	def test_furthest_from_origin(self):
		points = [data.Point(1,1), data.Point(3,4), data.Point(0,2)]
		expected = 1
		self.assertEqual(Lab5.furthest_from_origin(points), expected)

	def test_furthest_from_origin2(self):
		points = []
		expected = None
		self.assertEqual(Lab5.furthest_from_origin(points), expected)



if __name__ == '__main__':
    unittest.main()
