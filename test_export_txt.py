import pytest
import os
from tempfile import NamedTemporaryFile
from io import StringIO
from unittest.mock import patch
from datetime import datetime
from MainProgram import (
    Student,
    import_studentow,
    eksport_do_csv,
    eksport_do_txt,
    dodaj_nowego_studenta,
    edytuj_obecnosc,
    synchronizuj_obecnosc,
    sprawdz_obecnosc,
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
