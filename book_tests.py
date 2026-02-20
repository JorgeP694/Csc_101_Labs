from book_class import *
import unittest


class TestCases(unittest.TestCase):
    def test_Book_1(self):
        book = Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
        self.assertEqual(book.authors, ['Neil Gaiman', 'Terry Pratchett'])
        self.assertEqual(book.title, 'Good Omens')


    def test_Book_eq_1(self):
        book1 = Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
        book2 = Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
        self.assertEqual(book1, book2)


    def test_Book_eq_2(self):
        book = Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
        self.assertEqual(book, book)


    def test_Book_eq_3(self):
        book1 = Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
        book2 = Book(['Terry Pratchett', 'Neil Gaiman'], 'Good Omens')
        self.assertNotEqual(book1, book2)


    def test_Book_eq_4(self):
        book1 = Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
        book2 = Book(['Neil Gaiman', 'Terry Pratchett'],
            'Illustrated Good Omens')
        self.assertNotEqual(book1, book2)


    def test_Book_eq_5(self):
        book = Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
        other = 1.20
        self.assertNotEqual(book, other)


    def test_Book_repr(self):
        book = Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
        self.assertEqual(repr(book),
            "Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')")


if __name__ == '__main__':
    unittest.main()
