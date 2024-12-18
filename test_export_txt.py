import pytest
from tempfile import NamedTemporaryFile
from unittest.mock import patch
from MainProgram import (
    Student,
    eksport_do_txt
)
@pytest.fixture
def sample_students():
    return [
        Student("Jan", "Kowalski"),
        Student("Anna", "Nowak", True),
        Student("Marek", "Zieliński", False),
    ]

def test_eksport_do_txt_creates_file(sample_students):
    with NamedTemporaryFile(delete=False, mode='w', suffix='.txt') as temp_file:
        temp_file_path = temp_file.name

    eksport_do_txt(sample_students, temp_file_path)
    assert os.path.exists(temp_file_path)

    os.remove(temp_file_path)

def test_eksport_do_txt_correct_format(sample_students):
    with NamedTemporaryFile(delete=False, mode='w', suffix='.txt') as temp_file:
        temp_file_path = temp_file.name

    eksport_do_txt(sample_students, temp_file_path)
    
    with open(temp_file_path, 'r') as file:
        lines = file.readlines()
        assert len(lines) == 3
        assert "Jan Kowalski - Nieobecny\n" in lines
        assert "Anna Nowak - Obecny\n" in lines

    os.remove(temp_file_path)
