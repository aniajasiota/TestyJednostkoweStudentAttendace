import pytest
import os
from tempfile import NamedTemporaryFile
from io import StringIO
from unittest.mock import patch
from datetime import datetime
from MainProgram import (
    Student,
    synchronizuj_obecnosc
)
@pytest.fixture
def sample_students():
    return [
        Student("Jan", "Kowalski"),
        Student("Anna", "Nowak", True),
        Student("Marek", "Zieliński", False),
    ]

def test_synchronizuj_obecnosc_correct_update(sample_students):
    obecnosci = {
        sample_students[0]: True,
        sample_students[1]: False,
        sample_students[2]: True,
    }
    synchronizuj_obecnosc(sample_students, obecnosci)
    
    assert sample_students[0].attendance is True
    assert sample_students[1].attendance is False
    assert sample_students[2].attendance is True
