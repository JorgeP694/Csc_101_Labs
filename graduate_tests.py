# Project 3 Graduate Rate (2017-2018)
# Name:
# Instructor: Dr. S. Einakian
# Section: 

# unittest cases for graduate rate will include here
# At least two test cases for each function
import unittest
import os
import tempfile

from graduate_funcs import Division, Graduate, read_file, create_division, create_graduate, create_files

class TestCases(unittest.TestCase):
    def test_Division_Object_1(self):
        d = Division(3400, "Computer")
        self.assertEqual(d.id, 3400)

    def test_Division_Object_2(self):
        d = Division(3200, "Agriculture")
        self.assertEqual(d.division_name, "Agriculture")

    def test_Graduate_eq_true(self):
        g1 = Graduate(3401, "CS", (2, 10), (4, 3), (6, 5))
        g2 = Graduate(9999, "Other", (2, 10), (4, 3), (6, 5))
        self.assertEqual(g1, g2)

    def test_Graduate_eq_false(self):
        g1 = Graduate(3401, "CS", (2, 10), (4, 3), (6, 5))
        g2 = Graduate(3401, "CS", (1, 10), (4, 3), (6, 5))
        self.assertNotEqual(g1, g2)

    def _sample_csv(self):
        return (
            "h1\n"
            "h2\n"
            "h3\n"
            "3400,Computer,,,,,,\n"
            "3401,Computer science,10,2,3,4,5,6\n"
        )

    def _write_temp_csv(self, text):
        fd, path = tempfile.mkstemp(suffix=".csv")
        os.close(fd)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        return path

    def test_read_file_header_length(self):
        path = self._write_temp_csv(self._sample_csv())
        header, data = read_file(path)
        self.assertEqual(len(header), 3)

    def test_read_file_data_length(self):
        path = self._write_temp_csv(self._sample_csv())
        header, data = read_file(path)
        self.assertEqual(len(data), 2)

    def test_create_division_count(self):
        data = self._sample_csv().splitlines()[3:]
        divs = create_division(data)
        self.assertEqual(len(divs), 1)

    def test_create_division_id(self):
        data = self._sample_csv().splitlines()[3:]
        divs = create_division(data)
        self.assertEqual(divs[0].id, 3400)

    def test_create_graduate_count(self):
        data = self._sample_csv().splitlines()[3:]
        grads = create_graduate(data)
        self.assertEqual(len(grads), 1)

    def test_create_graduate_tuple_order(self):
        data = self._sample_csv().splitlines()[3:]
        grads = create_graduate(data)
        self.assertEqual(grads[0].bachelor, (2, 10))

    def test_create_files_creates_file(self):
        with tempfile.TemporaryDirectory() as td:
            cwd = os.getcwd()
            os.chdir(td)
            try:
                data = self._sample_csv().splitlines()[3:]
                divs = create_division(data)
                grads = create_graduate(data)
                create_files(divs, grads)
                self.assertTrue(os.path.exists("computer.csv"))
            finally:
                os.chdir(cwd)

    def test_create_files_writes_correct_header(self):
        with tempfile.TemporaryDirectory() as td:
            cwd = os.getcwd()
            os.chdir(td)
            try:
                data = self._sample_csv().splitlines()[3:]
                divs = create_division(data)
                grads = create_graduate(data)
                create_files(divs, grads)

                with open("computer.csv", "r") as f:
                    lines = f.readlines()

                self.assertEqual(lines[1].strip(),
                                 "ID,Major,Bachelor,Master,Doctor")
            finally:
                os.chdir(cwd)



# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
