import pytest
import os
from tempfile import NamedTemporaryFile
from unittest.mock import patch
from MainProgram import (
    Student,
    dodaj_nowego_studenta
)
@pytest.fixture
def sample_students():
    return [
        Student("Jan", "Kowalski"),
        Student("Anna", "Nowak", True),
        Student("Marek", "Zieliński", False),
    ]

def test_dodaj_nowego_studenta_correct_input(sample_students):
    with patch("builtins.input", side_effect=["Katarzyna", "Wiśniewska", "tak"]):
        dodaj_nowego_studenta(sample_students)
    
    assert len(sample_students) == 4
    assert sample_students[-1].name == "Katarzyna"
    assert sample_students[-1].surname == "Wiśniewska"
    assert sample_students[-1].attendance is True

def test_dodaj_nowego_studenta_incorrect_input(sample_students):
    with patch("builtins.input", side_effect=["Katarzyna", "Wiśniewska", "nie"]):
        dodaj_nowego_studenta(sample_students)
    
    assert len(sample_students) == 4
    assert sample_students[-1].attendance is False
