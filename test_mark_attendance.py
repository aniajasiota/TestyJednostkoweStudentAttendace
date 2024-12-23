import unittest
from unittest.mock import patch
from import_eksport_files import mark_attendance

class TestMarkAttendance(unittest.TestCase):

    @patch('builtins.input', side_effect=["y", "n"])
    def test_mark_attendance(self, mock_input):
        students = [{'name': 'John', 'present': False}, {'name': 'Jane', 'present': False}]
        mark_attendance(students)
        self.assertTrue(students[0]['present'])
        self.assertFalse(students[1]['present'])


if __name__ == '__main__':
    unittest.main()