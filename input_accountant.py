command = []

with open("in.txt", "r") as file:
    for row in file:
        command.append(row.strip())
list = []
command_final = []

for i, j in enumerate(command):
    if j == "saldo":
        list.append(command[i])
        list.append(command[i + 1])
        list.append(command[i + 2])
        command_final.append(list)
        list = []
    elif j == "sprzedaz":
        list.append(command[i])
        list.append(command[i + 1])
        list.append(command[i + 2])
        list.append(command[i + 3])
        command_final.append(list)
        list = []
    elif j == "zakup":
        list.append(command[i])
        list.append(command[i + 1])
        list.append(command[i + 2])
        list.append(command[i + 3])
        command_final.append(list)
        list = []
    elif j == "konto":
        list.append(command[i])
        command_final.append(list)
        list = []
    elif j == "magazyn":
        list.append(command[i])
        list.append(command[i + 1])
        list.append(command[i + 2])
        list.append(command[i + 3])
        list.append(command[i + 4])
        command_final.append(list)
        list = []
    elif j == "przeglad":
        list.append(command[i])
        command_final.append(list)
        list = []
    elif j == "stop":
        list.append(command[i])
        command_final.append(list)
        list = []

#print(command_final)


