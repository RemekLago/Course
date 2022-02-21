from pprint import pprint
import sys

def open_file_with_history():
    """open file to import history of school base
    and split it to list of lists"""
    command_input_history = []

    with open("input_lesson_4_schoolbase.txt", "r") as file:
        for row in file:
            command_input_history.append(row.strip())

    list_temporary = []
    command_input_final = []
    for idx, idy in enumerate(command_input_history):
        if idy == "uczen":
            command_input_history.insert(idx+3, "")

    for idx in command_input_history:
        if idx != "":
            list_temporary.append(idx)
        elif idx == "":
            command_input_final.append(list_temporary)
            list_temporary = []
        elif idx == "koniec":
            break
    return command_input_final


class Student:
    def __init__(self, status, imie, klasa, przedmiot=None):
        self.status = status
        self.imie = imie
        self.przedmiot = przedmiot
        self.klasa = klasa


class Teacher:
    def __init__(self, status, imie, przedmiot, klasa):
        self.imie = imie
        self.status = status
        self.klasa = klasa
        self.przedmiot = przedmiot


class Tutor:
    def __init__(self, status, imie, klasa):
        self.imie = imie
        self.status = status
        self.klasa = klasa


data = open_file_with_history()
students = []
teachers = []
tutors = []


def create_list_of_students():
    """create a list of students"""
    for idy in data:
        if idy[0] == "uczen":
            person = Student(idy[0], idy[1], idy[2])
            students.append(person)
            continue
        else:
            continue
    print("zrobione")
    return students


def create_list_of_teachers():
    """create a list of teachers"""
    for idy in data:
        if idy[0] == "nauczyciel":
            status = idy[0]
            imie = idy[1]
            przedmiot = idy[2]
            klasa = idy[3]
            person = Teacher(status, imie, przedmiot, klasa)
            teachers.append(person)
            continue
        else:
            continue
    print("zrobione")
    return teachers


def create_list_of_tutors():
    """create a list of tutors"""
    for idy in data:
        if idy[0] == "wychowawca":
            status = idy[0]
            imie = idy[1]
            klasa = idy[2]
            person = Tutor(status, imie, klasa)
            tutors.append(person)
            continue
        else:
            continue
    print("zrobione")
    return tutors









# with open("output_lesson_4_schoolbase_class.txt", "w") as file:
#     i = take_input_and_report()
#     for element in i:
#         file.write(element + "\n")