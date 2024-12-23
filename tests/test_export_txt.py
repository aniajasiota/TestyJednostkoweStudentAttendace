import unittest
from unittest.mock import patch, mock_open

class TestExportStudentsTXT(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open)
    def test_export_students_txt(self, mock_open):
        from import_eksport_files import export_students_txt
        students = [{'name': 'John', 'present': True}, {'name': 'Jane', 'present': False}]
        export_students_txt(students, "output.txt")
        mock_open.assert_called_with("output.txt", mode='w')
        mock_open().write.assert_any_call("John: Present\n")
        mock_open().write.assert_any_call("Jane: Absent\n")


if __name__ == '__main__':
    unittest.main()