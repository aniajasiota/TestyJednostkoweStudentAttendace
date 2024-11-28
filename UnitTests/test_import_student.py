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

def test_import_studentow_correct_file():
    with NamedTemporaryFile(delete=False, mode='w') as temp_file:
        temp_file.write("Jan Kowalski\nAnna Nowak\n")
        temp_file_path = temp_file.name
    
    students = import_studentow(temp_file_path)
    
    assert len(students) == 2
    assert students[0].name == "Jan"
    assert students[0].surname == "Kowalski"
    assert students[1].name == "Anna"
    assert students[1].surname == "Nowak"
    
    os.remove(temp_file_path)

def test_import_studentow_file_not_found():
    students = import_studentow("non_existing_file.txt")
    assert students == []
