import sys
from termcolor import colored
from input_accountant import command_final

print(command_final)
history_account = []
balance_start = 0
product_dict = {}

nowa_akcja = sys.argv
command_final.append(nowa_akcja[1:])

for i, j in enumerate(command_final):
    data_input = command_final[i]
    if data_input[0] == "saldo":
        balance = int(data_input[1])
        comment = data_input[2]
        history_account.append(data_input)
        balance_start += balance

    elif data_input[0] == "zakup":
        product_id = data_input[1]
        price = int(data_input[2])
        quantity = int(data_input[3])
        balance_start -= price * quantity
        if product_dict.get(f"{product_id}"):
            product_dict[product_id] = product_dict[product_id] + quantity
        elif not product_dict.get(f"{product_id}"):
            product_dict.update({product_id: quantity})
            print(f"Zakup: {product_id} {quantity}")
            print(product_dict)
        elif balance_start < 0:     # or balance_start < price * quantity:
            print("ERROR - balance lower than 0")
        elif price < 0:
            print("ERROR - price lower than 0")
        elif quantity < 0:
            print("ERROR - quantity lower than 0")
        history_account.append(data_input)

    elif data_input[0] == "sprzedaz":
        product_id = data_input[1]
        price = int(data_input[2])
        quantity = int(data_input[3])
        balance_start += price * quantity
        if product_dict.get(f"{product_id}") >= quantity:
            product_dict[product_id] -= quantity
        elif product_dict.get(f"{product_id}") < quantity:
            print("ERROR - quantity after sale lower than 0")
        if price < 0:
            print("ERROR - price lower than 0")
        if quantity < 0:
            print("ERROR - quantity lower than 0")
        history_account.append(data_input)
        print(f"Sprzedaz: {product_id} {product_dict[product_id]}")
        print(product_dict)

    elif data_input[0] == "konto":
        print(f"{balance_start}")
        history_account.append(data_input)

    elif data_input[0] == "magazyn":
        for key in product_dict:
            print(f"{key} {product_dict[key]}")
        history_account.append(data_input)

    elif data_input[0] == "przeglad":
        print(f"{history_account}")
        history_account.append(data_input)

    elif data_input[0] == "stop":
        pass
        history_account.append(data_input)

    else:
        print("ERROR")
        history_account.append(data_input)

    print(colored(f"product_dict: {product_dict}", "yellow"))
    print(colored(f"balance_start: {balance_start}", "yellow"))
    print(colored(f"history_account: {history_account}", "yellow"))
    print("-" * 100)

for akcja in history_account:
    for element in akcja:
        print(element)


# with open("out.txt", "w") as file:
#     for i, j in history_account:
#         file.write('a1 ')
#
#     file.close()

