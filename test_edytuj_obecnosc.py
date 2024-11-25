import pytest
import os
from tempfile import NamedTemporaryFile
from io import StringIO
from unittest.mock import patch
from datetime import datetime
from testyJednostkoweProgram import (
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

def test_edytuj_obecnosc_correct_input(sample_students):
    obecnosci = {student: student.obecnosc for student in sample_students}
    with patch("builtins.input", side_effect=["tak", "nie", "tak"]):
        edytuj_obecnosc(obecnosci)
    
    assert obecnosci[sample_students[0]] is True
    assert obecnosci[sample_students[1]] is False
    assert obecnosci[sample_students[2]] is True
