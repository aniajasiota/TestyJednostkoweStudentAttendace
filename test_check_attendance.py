import pytest
from tempfile import NamedTemporaryFile
from unittest.mock import patch
from MainProgram import (
    Student,
    sprawdz_obecnosc
)
@pytest.fixture
def sample_students():
    return [
        Student("Jan", "Kowalski"),
        Student("Anna", "Nowak", True),
        Student("Marek", "Zieliński", False),
    ]

def test_sprawdz_obecnosc_correct_input(sample_students):
    with patch("builtins.input", side_effect=["tak", "nie", "tak"]):
        sprawdz_obecnosc(sample_students)
    
    assert sample_students[0].attendance is True
    assert sample_students[1].attendance is False
    assert sample_students[2].attendance is True
