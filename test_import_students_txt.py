import unittest
from unittest.mock import patch, mock_open
from import_eksport_files import import_students_txt

class TestImportStudentsTXT(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data="John\nJane\n")
    def test_import_students_txt(self, mock_open):
        students = import_students_txt("students.txt")
        expected = [{'name': 'John', 'present': False}, {'name': 'Jane', 'present': False}]
        self.assertEqual(students, expected)


if __name__ == '__main__':
    unittest.main()