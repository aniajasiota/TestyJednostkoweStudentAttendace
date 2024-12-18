import pytest
from tempfile import NamedTemporaryFile
from unittest.mock import patch
from MainProgram import (
    Student,
    edytuj_obecnosc
)
@pytest.fixture
def sample_students():
    return [
        Student("Jan", "Kowalski"),
        Student("Anna", "Nowak", True),
        Student("Marek", "Zieliński", False),
    ]

def test_edytuj_obecnosc_correct_input(sample_students):
    obecnosci = {student: student.attendance for student in sample_students}
    with patch("builtins.input", side_effect=["tak", "nie", "tak"]):
        edytuj_obecnosc(obecnosci)
    
    assert obecnosci[sample_students[0]] is True
    assert obecnosci[sample_students[1]] is False
    assert obecnosci[sample_students[2]] is True
