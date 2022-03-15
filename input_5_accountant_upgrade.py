def open_file():
    command = []
    with open("in2.txt", "r") as file:
        for row in file:
            command.append(row.strip())
    return command


def check_kind_of_input():
    """preparation data from file in2.txt as a input to file 'accountant'"""
    list_temporary = []
    command_final = []
    command = open_file()
    for i, j in enumerate(command):
        if j == "saldo":
            list_temporary.append(command[i])
            list_temporary.append(command[i + 1])
            list_temporary.append(command[i + 2])
            command_final.append(list_temporary)
            list_temporary = []
        elif j == "sprzedaz":
            list_temporary.append(command[i])
            list_temporary.append(command[i + 1])
            list_temporary.append(command[i + 2])
            list_temporary.append(command[i + 3])
            command_final.append(list_temporary)
            list_temporary = []
        elif j == "zakup":
            list_temporary.append(command[i])
            list_temporary.append(command[i + 1])
            list_temporary.append(command[i + 2])
            list_temporary.append(command[i + 3])
            command_final.append(list_temporary)
            list_temporary = []
        elif j == "konto":
            list_temporary.append(command[i])
            command_final.append(list_temporary)
            list_temporary = []
        elif j == "magazyn":
            list_temporary.append(command[i])
            list_temporary.append(command[i + 1])
            list_temporary.append(command[i + 2])
            list_temporary.append(command[i + 3])
            command_final.append(list_temporary)
            list_temporary = []
        elif j == "przeglad":
            list_temporary.append(command[i])
            command_final.append(list_temporary)
            list_temporary = []
        elif j == "stop":
            list_temporary.append(command[i])
            command_final.append(list_temporary)
            list_temporary = []
    return command_final




