import convert
import unittest
from convert import str_to_float


class TestStrToFloat(unittest.TestCase):
    def test_valid_integer_string(self) -> None:
        self.assertEqual(str_to_float("3.0"), 3.0)

    def test_valid_float_string(self) -> None:
        self.assertEqual(str_to_float("4.73"), 4.73)

    def test_valid_negative(self) -> None:
        self.assertEqual(str_to_float("-2.5"), -2.5)

    def test_valid_with_whitespace(self) -> None:
        self.assertEqual(str_to_float("  7.5 "), 7.5)

    def test_invalid_letters(self) -> None:
        self.assertIsNone(str_to_float("xyz"))

    def test_empty_string(self) -> None:
        self.assertIsNone(str_to_float(""))

    def test_garbage_mixed(self) -> None:
        self.assertIsNone(str_to_float("12.3.4"))

    def test_none_input_defensive(self) -> None:
        self.assertIsNone(str_to_float(None))

if __name__ == "__main__":
    unittest.main()