import sys
from termcolor import colored
from input_accountant import command_final

history_account = []
balance_start = 0
product_dict = {}

"""add a task from input to the previous history updated from file in.txt
remove command stop and than add it on the end of list"""
command_stop = ["stop"]
command_final.remove(command_stop)
new_command_input = sys.argv
command_final.append(new_command_input[1:])
command_final.append(command_stop)

"loop with all 'if' and adding operation to list with history"
for data_input in command_final:
    if data_input[0] == "saldo":
        balance = int(data_input[1])
        comment = data_input[2]
        history_account.append(data_input)
        if balance_start + balance < 0:
            print("ERROR - not enough money on account")
        else:
            balance_start += balance

    elif data_input[0] == "zakup":
        product_id = data_input[1]
        price = int(data_input[2])
        quantity = int(data_input[3])
        if balance_start - price * quantity < 0:
            print("ERROR - not enough money on account")
        elif price < 0:
            print("ERROR - price lower than 0")
        elif quantity < 0:
            print("ERROR - quantity lower than 0")
        else:
            balance_start -= price * quantity
            if product_dict.get(f"{product_id}"):
                product_dict[product_id] = product_dict[product_id] + quantity
            elif not product_dict.get(f"{product_id}"):
                product_dict.update({product_id: quantity})
#                print(f"Zakup: {product_id} {quantity}")
#                print(product_dict)
            history_account.append(data_input)

    elif data_input[0] == "sprzedaz":
        product_id = data_input[1]
        price = int(data_input[2])
        quantity = int(data_input[3])
        balance_start += price * quantity
        if product_dict.get(f"{product_id}") < quantity:
            print("ERROR - quantity after sale lower than 0")
        elif price < 0:
            print("ERROR - price lower than 0")
        elif quantity < 0:
            print("ERROR - quantity lower than 0")
        elif product_dict.get(f"{product_id}") >= quantity:
            product_dict[product_id] -= quantity
        history_account.append(data_input)
#        print(f"Sprzedaz: {product_id} {product_dict[product_id]}")
#        print(product_dict)

    elif data_input[0] == "konto":
        print(f"{balance_start}")

    elif data_input[0] == "magazyn":
        for key in product_dict:
            print(f"{key} {product_dict[key]}")

    elif data_input[0] == "przeglad":
        print(f"{history_account}")

    elif data_input[0] == "stop":
        history_account.append(data_input)
        break

    else:
        print("ERROR")

"writing to file all history of accounting process"
with open("out.txt", "w") as file:
    for i in history_account:
        for element in i:
            file.write(element + "\n")

#    print(colored(f"product_dict: {product_dict}", "yellow"))
#    print(colored(f"balance_start: {balance_start}", "yellow"))
#    print(colored(f"history_account: {history_account}", "yellow"))
#    print("-" * 100)




