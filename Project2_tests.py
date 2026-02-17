
#Name:
#Section: 
import classes
import Project2
import unittest


# Write two test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle(self):
        r = Project2.create_rectangle(classes.Point(2, 2), classes.Point(10, 10))
        self.assertEqual(r, classes.Rectangle(classes.Point(2, 10), classes.Point(10, 2)))

    def test_create_rectangle2(self):
        r = Project2.create_rectangle(classes.Point(5, 1), classes.Point(1, 5))
        self.assertEqual(r, classes.Rectangle(classes.Point(1, 5), classes.Point(5, 1)))

    # Part 2
    def test_shorter_duration_than(self):
        self.assertTrue(Project2.shorter_duration_than(classes.Duration(3, 0), classes.Duration(4, 0)))

    def test_shorter_duration_than2(self):
        self.assertFalse(Project2.shorter_duration_than(classes.Duration(5, 0), classes.Duration(4, 59)))

    # Part 3
    def test_songs_shorter_than(self):
        songs = [
            classes.Song("A", "S1", classes.Duration(3, 0)),
            classes.Song("B", "S2", classes.Duration(5, 0))
        ]
        result = Project2.songs_shorter_than(songs, classes.Duration(4, 0))
        self.assertEqual(result, [songs[0]])

    def test_songs_shorter_than2(self):
        songs = []
        result = Project2.songs_shorter_than(songs, classes.Duration(4, 0))
        self.assertEqual(result, [])

    # Part 4
    def test_running_time(self):
        songs = [
            classes.Song("A", "S1", classes.Duration(4, 30)),
            classes.Song("B", "S2", classes.Duration(3, 30))
        ]
        total = Project2.running_time(songs, [0, 1])
        self.assertEqual(total, classes.Duration(8, 0))

    def test_running_time2(self):
        songs = [
            classes.Song("A", "S1", classes.Duration(2, 0))
        ]
        total = Project2.running_time(songs, [0, 5, -1])
        self.assertEqual(total, classes.Duration(2, 0))

    # Part 5
    def test_validate_route(self):
        links = [
            ["a", "b"],
            ["b", "c"]
        ]
        self.assertTrue(Project2.validate_route(links, ["a", "b", "c"]))

    def test_validate_route2(self):
        links = [
            ["a", "b"]
        ]
        self.assertFalse(Project2.validate_route(links, ["a", "c"]))
    
    # Part 6
    def test_longest_repetition(self):
        self.assertEqual(Project2.longest_repetition([1, 1, 2, 2, 1, 1, 1, 3]), 4)

    def test_longest_repetition2(self):
        self.assertIsNone(Project2.longest_repetition([]))

if __name__ == '__main__':
    unittest.main()
