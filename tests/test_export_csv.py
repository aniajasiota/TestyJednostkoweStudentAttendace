import unittest
from unittest.mock import patch, mock_open, MagicMock
import csv
from import_eksport_files import export_students_csv

class TestExportStudentsCSV(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open)
    @patch('csv.writer')
    def test_export_students_csv(self, mock_writer, mock_open):
        students = [{'name': 'John', 'present': True}, {'name': 'Jane', 'present': False}]
        
        export_students_csv(students, "output.csv")
        mock_open.assert_called_with("output.csv", mode='w', newline='')
        mock_writer.return_value.writerow.assert_any_call(['Name', 'Present'])
        mock_writer.return_value.writerow.assert_any_call(['John', True])
        mock_writer.return_value.writerow.assert_any_call(['Jane', False])

if __name__ == '__main__':
    unittest.main()