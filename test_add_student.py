import unittest
from unittest.mock import patch
from main import add_student

class TestAddStudent(unittest.TestCase):

    @patch('builtins.input', side_effect=["John", "Doe", "12345"])
    def test_add_student(self, mock_input):   
        expected = "John,Doe,12345\n"
        self.assertEqual(add_student(), expected)


if __name__ == '__main__':
    unittest.main()