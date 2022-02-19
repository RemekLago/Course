from pprint import pprint

def open_file_with_history():
    """open file to import history of school base
    and split it to list of lists"""
    command_input = []

    with open("input_lesson_4_schoolbase.txt", "r") as file:
        for row in file:
            command_input.append(row.strip())

    list_temporary = []
    command_input_final = []

    for idx in command_input:
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
    command_input_final = open_file_with_history()

    student_list = [i for i in command_input_final if i[0] == "uczen"]
    teacher_list = [i for i in command_input_final if
                    i[0] == "wychowawca" or i[0] == "nauczyciel"]

    print(student_list)
    print(teacher_list)
    dict_of_persons = {}

    for idx, idy in enumerate(student_list[0]):
        if idy == "uczen":
            dict_of_persons[student_list[0][idx + 1]] = \
                {
                "status": student_list[0][idx],
                "klasa": student_list[0][idx + 2]
            }

    # for idx, idy in enumerate(teacher_list):
    #     x = len(idy)
    #     if idy[0] == "wychowawca":
    #         dict_of_persons[teacher_list[idx][idx + 1]] = {
    #             "status": teacher_list[idx][idx], "klasa": teacher_list[idx][idx + 2]
    #         }
        # elif idy == "nauczyciel":
        #     dict_of_persons[command_input[idx + 1]] = {
        #         "status": command_input[idx], "klasa": command_input[idx + 3],
        #         "przedmiot": command_input[idx + 2]
        #     }
    pprint(dict_of_persons)


dictionary_with_staff()