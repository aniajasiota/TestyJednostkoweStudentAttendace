import unittest
from unittest.mock import patch, mock_open
from io import StringIO
import os
from main import manage_student_file

class TestManageStudentFile(unittest.TestCase):

    @patch('main.add_student', return_value="John,Doe,125\n")
    @patch('builtins.input', side_effect=["yes"])
    @patch('os.path.isfile', return_value=False)
    @patch('builtins.open', new_callable=mock_open)
    def test_create_new_file(self, mock_open, mock_isfile, mock_input, mock_add_student):
        """
        Testuje tworzenie nowego pliku i dodanie studenta.
        """
        manage_student_file()
        # Sprawdzenie, czy plik został otwarty w trybie 'a' (append)
        mock_open.assert_called_with("list.txt", mode='a')
        # Sprawdzenie, czy nagłówek został zapisany
        mock_open().write.assert_any_call("First Name,Last Name,ID\n")
        # Sprawdzenie, czy dane studenta zostały zapisane
        mock_open().write.assert_any_call("John,Doe,125\n")

    @patch('builtins.input', side_effect=["no"])
    @patch('os.path.isfile', return_value=True)
    def test_no_addition(self, mock_isfile, mock_input):
        """
        Testuje przerwanie operacji, gdy plik istnieje i użytkownik wybiera 'no'.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            manage_student_file()
            # Sprawdzenie, czy komunikat o przerwaniu operacji został wyświetlony
            self.assertIn("Operation terminated.", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()