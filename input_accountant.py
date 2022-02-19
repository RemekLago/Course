command = []

with open("in.txt", "r") as file:
    for row in file:
        command.append(row.strip())
list_temporary = []
command_final = []

"preparation data from file in.txt as a input to file 'accountant'"
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
        list_temporary.append(command[i + 4])
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

#print(command_final)


