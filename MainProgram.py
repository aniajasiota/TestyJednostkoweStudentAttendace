import os
import csv
from datetime import datetime

class Student:
    def __init__(self, name, surname, attendance=False):
        self.name = name
        self.surname = surname
        self.attendance = attendance

    def __str__(self):
        return f"{self.name} {self.surname} - {'Obecny' if self.attendance else 'Nieobecny'}"

    def to_csv(self):
        return f"{self.name},{self.surname},{'Obecny' if self.attendance else 'Nieobecny'}"


def import_studentow(file_path):
    studenci = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(' ')
                if len(data) >= 2:
                    studenci.append(Student(data[0], data[1]))
    else:
        print("Plik nie istnieje.")
    return studenci


def eksport_do_csv(studenci, file_path):
    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["name", "surname", "Obecny"])
            for student in studenci:
                writer.writerow([student.name, student.surname, "Obecny" if student.attendance else "Nieobecny"])
        print(f"Zapisano plik CSV: {file_path}")
    except Exception as ex:
        print(f"Błąd przy zapisie pliku CSV: {ex}")


def eksport_do_txt(studenci, file_path):
    try:
        with open(file_path, 'w') as file:
            for student in studenci:
                file.write(str(student) + '\n')
        print(f"Zapisano plik TXT: {file_path}")
    except Exception as ex:
        print(f"Błąd przy zapisie pliku TXT: {ex}")


def dodaj_nowego_studenta(studenci):
    name = input("Podaj imię studenta: ")
    surname = input("Podaj surname studenta: ")
    attendance = input("Czy student jest obecny? (tak/nie): ").strip().lower() == 'tak'
    nowy_student = Student(name, surname, attendance)
    studenci.append(nowy_student)
    print(f"Dodano nowego studenta: {nowy_student}")


def edytuj_obecnosc(obecnosci):
    print("Edycja obecności studentów:")
    for student in obecnosci:
        obecny = input(f"Czy {student.name} {student.surname} jest obecny? (tak/nie): ").strip().lower() == 'tak'
        obecnosci[student] = obecny


def synchronizuj_obecnosc(studenci, obecnosci):
    for student in studenci:
        if student in obecnosci:
            student.attendance = obecnosci[student]


def sprawdz_obecnosc(studenci):
    for student in studenci:
        obecny = input(f"Czy {student.name} {student.surname} jest obecny? (tak/nie): ").strip().lower() == 'tak'
        student.attendance = obecny


def main():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    input_file_path = os.path.join(desktop_path, "Obecni.txt")

    studenci = import_studentow(input_file_path)

    if not studenci:
        print("Plik nie zawiera studentów lub nie istnieje.")
        return

    data_input = input("Podaj dzisiejszą datę (dd-mm-YY): ")
    data = datetime.strptime(data_input, "%d-%m-%Y")

    if input("Czy chcesz sprawdzić obecność studentów? (tak/nie): ").strip().lower() == 'tak':
        sprawdz_obecnosc(studenci)

    print("Lista studentów:")
    for student in studenci:
        print(student)

    if input("Czy chcesz dodać nowego studenta? (tak/nie): ").strip().lower() == 'tak':
        dodaj_nowego_studenta(studenci)

    obecnosci = {student: student.attendance for student in studenci}

    if input("Czy chcesz edytować listę obecności? (tak/nie): ").strip().lower() == 'tak':
        edytuj_obecnosc(obecnosci)

    synchronizuj_obecnosc(studenci, obecnosci)

    format_zapisu = input("Podaj format zapisu txt/csv: ").strip().lower()
    output_file_path = os.path.join(desktop_path, "Obecni_Export.csv" if format_zapisu == 'csv' else "Obecni_Export.txt")

    if format_zapisu == 'csv':
        eksport_do_csv(studenci, output_file_path)
    elif format_zapisu == 'txt':
        eksport_do_txt(studenci, output_file_path)
    else:
        print("Nieznany format.")

    print(f"Zapisano plik na pulpicie: {output_file_path}")


if __name__ == "__main__":
    main()
