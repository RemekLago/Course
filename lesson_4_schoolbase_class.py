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
#students = []
#teachers = []
#tutors = []
students = {}
teachers = {}
tutors = {}

def create_dict_of_students():
    """create a dictionary of students"""
    for idy in data:
        if idy[0] == "uczen":
            person = Student(idy[0], idy[1], idy[2])
            students.update({person.imie: {"status": person.status, "klasa": person.klasa}})
            continue
        else:
            continue
#    print(students)
    return students


def create_dict_of_teachers():
    """create a dict of teachers"""
    for idy in data:
        if idy[0] == "nauczyciel":
            status = idy[0]
            imie = idy[1]
            przedmiot = idy[2]
            list_class = [j for i, j in enumerate(idy) if i >= 3]
            klasa = list_class
            person = Teacher(status, imie, przedmiot, klasa)
            teachers.update({person.imie: {"status": person.status,
                                           "klasa": person.klasa,
                                           "przedmiot": person.przedmiot}})
            continue
        else:
            continue
#    print(teachers)
    return teachers


def create_dict_of_tutors():
    """create a dict of tutors"""
    for idy in data:
        if idy[0] == "wychowawca":
            status = idy[0]
            imie = idy[1]
            list_class = [j for i, j in enumerate(idy) if i >= 2]
            klasa = list_class
            person = Tutor(status, imie, klasa)
            tutors.update({person.imie: {"status": person.status,
                                         "klasa": person.klasa}})
            continue
        else:
            continue
#    print(tutors)
    return tutors


def merge_dictionaries():
    """merge all dictionaries to one for better searching in next steps"""
    d1 = create_dict_of_students()
    d2 = create_dict_of_teachers()
    d3 = create_dict_of_tutors()

    dictionary_all = d1 | d2 | d3
#    print(dictionary_all)
    return dictionary_all


def searching_result_for_command():
    """ """
    data_history = merge_dictionaries()
#    print(data_history)
    x = sys.argv
    data_input = x[1:][0]
    result = []

    for key, value in data_history.items():
        if data_input in value["klasa"] and value["status"] == "wychowawca":
            result.append(key)
            names_classes = value["klasa"]
            for key1, value1 in data_history.items():
                if value1["klasa"] in names_classes:
                    result.append(key1)
        if data_input in key and value["status"] == "wychowawca":
            result.append(key)
            names_classes = value["klasa"]
            for key1, value1 in data_history.items():
                if value1["klasa"] in names_classes:
                    result.append(key1)

        if data_input in key and value["status"] == "nauczyciel":
            result.append(key)
            names_classes = value["klasa"]
            for key1, value1 in data_history.items():
                for i in value1["klasa"]:
                    if i in names_classes and value1["status"] == "wychowawca":
                        result.append(key1)

        if data_input in key and value["status"] == "uczen":
            result.append(key)
            names_classes = value["klasa"]
            for key1, value1 in data_history.items():
                if names_classes in value1["klasa"] and \
                        value1["status"] == "nauczyciel":
                    result.append(key1)
                    result.append(value1["przedmiot"])
#    pprint(result)
    return result


with open("output_lesson_4_schoolbase_class.txt", "w") as file:
    i = searching_result_for_command()
    for element in i:
        file.write(element + "\n")


