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

    for idx in command_input_history:
        if idx != "" and idx != "koniec":
            list_temporary.append(idx)
        elif idx == "":
            command_input_final.append(list_temporary)
            list_temporary = []
        elif idx == "koniec":
            command_input_final.append(list_temporary)
            break
    return command_input_final


def dictionary_with_staff():
    """Create a dictionary with all parameters
    from the file with initial data"""
    command_input_final = open_file_with_history()

    student_list = [i for i in command_input_final if i[0] == "uczen"]
    teacher_list = [i for i in command_input_final if
                    i[0] == "wychowawca" or i[0] == "nauczyciel"]

#    print(teacher_list)
    dict_of_students = {}
    dict_of_teachers = {}

    for idx, idy in enumerate(student_list[0]):
        if idy == "uczen":
            dict_of_students[student_list[0][idx + 1]] = \
                {
                 "imie_nazwisko": student_list[0][idx + 1],
                "status": student_list[0][idx],
                "klasa": [student_list[0][idx + 2]]
                }
    for record in teacher_list:
        for idx, idy in enumerate(record):
            if idy == "wychowawca":
                class_list = [i for i in record[idx + 2: len(record)+1]]
                dict_of_teachers[record[idx + 1]] =\
                    {
                    "imie_nazwisko": record[idx + 1],
                    "status": record[idx],
                    "klasa": class_list
                    }
    for record in teacher_list:
        for idx, idy in enumerate(record):
            if idy == "nauczyciel":
                class_list = [i for i in record[idx + 3: len(record)+1]]
                dict_of_teachers[record[idx + 1]] = \
                    {
                    "imie_nazwisko": record[idx + 1],
                    "status": record[idx],
                    "klasa": class_list,
                    "przedmiot": record[idx + 2]
                    }
#    pprint(dict_of_students)
#    pprint(dict_of_teachers)
    return dict_of_students, dict_of_teachers


def report_generating_class(data):
    """when input is name/number of class, function generate report
    with data: students names from this class and tutor's name"""
    input_command = data
    var = dictionary_with_staff()
    dict_of_students = var[0]
    dict_of_teachers = var[1]
    list_with_results = []

    for value in dict_of_teachers.values():
        if input_command in value["klasa"] and value["status"] == "wychowawca":
            list_with_results.append(value["imie_nazwisko"])
    for value in dict_of_students.values():
        if input_command in value["klasa"]:
            list_with_results.append(value["imie_nazwisko"])
    return list_with_results

def report_generating_tutor(data):
    """when input is name of tutor, function generate report
    with data: students names from all tutor's classes"""

    input_command = data
    var = dictionary_with_staff()
    dict_of_students = var[0]
    dict_of_teachers = var[1]
    list_with_results = []

    for value in dict_of_teachers.values():
        if input_command in value["imie_nazwisko"]:
            list_with_results.append(value["imie_nazwisko"])
            y = value["klasa"]
            for value2 in dict_of_students.values():
                if value2["klasa"][0] in y:
                    list_with_results.append(value2["imie_nazwisko"])
            return list_with_results


def report_generating_teacher(data):
    """when input is name of teacher, function generate report
    with data: tutor's names from all classes where teacher teaches"""

    input_command = data
    var = dictionary_with_staff()
    dict_of_students = var[0]
    dict_of_teachers = var[1]
    list_with_results = []
    set_with_results = set()

    for value in dict_of_teachers.values():
        if input_command in value["imie_nazwisko"]:
            set_with_results.add(value["imie_nazwisko"])
            y = value["klasa"]
    for value2 in dict_of_teachers.values():
        if value2["status"] == "wychowawca":
            for idx in value2["klasa"]:
                if idx in y:
                    set_with_results.add(value2["imie_nazwisko"])
    for idy in set_with_results:
        list_with_results.append(idy)
    return list_with_results


def report_generating_student(data):
    """when input is name of student, function generate report
    with data:names of subjects which student learners and
    teacher's names of that subjects"""

    input_command = data
    var = dictionary_with_staff()
    dict_of_students = var[0]
    dict_of_teachers = var[1]
    list_with_results = []

    for value in dict_of_students.values():
        if input_command in value["imie_nazwisko"]:
            list_with_results.append(value["imie_nazwisko"])
            y = value["klasa"]
            for value in dict_of_teachers.values():
                if value["status"] == "nauczyciel":
                    for idx in value["klasa"]:
                        if idx in y:
                            list_with_results.append(value["przedmiot"])
                            list_with_results.append(value["imie_nazwisko"])
    return list_with_results


def take_input_and_report():
    """it takes input and find what input means: class, student, teacher
    or tutor. Then start the right method and write it to output file"""

    x = sys.argv
    command_input = x[1:][0]
    var = dictionary_with_staff()
    dict_of_students = var[0]
    dict_of_teachers = var[1]

    for value in dict_of_teachers.values():
        if command_input in value["klasa"] and value["status"] == "wychowawca":
            i = report_generating_class(command_input)
            return i
        if command_input in value["imie_nazwisko"] and value["status"] == "wychowawca":
            i = report_generating_tutor(command_input)
            return i
        if command_input in value["imie_nazwisko"] and value["status"] == "nauczyciel":
            i = report_generating_teacher(command_input)
            return i
    for value in dict_of_students.values():
        if command_input in value["imie_nazwisko"]:
            i = report_generating_student(command_input)
            return i


with open("output_lesson_4_schoolbase.txt", "w") as file:
    i = take_input_and_report()
    for element in i:
        file.write(element + "\n")

take_input_and_report()