from termcolor import colored
from input_accountant_upgrade import check_kind_of_input


def running_process():
    command_final = check_kind_of_input()
    history_account = []
    balance_start = 0
    product_dict = {}
    data_temporary = []
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

        elif data_input[0] == "konto":
#            print(f"{balance_start}")
            data_temporary.append("konto")
            data_temporary.append(balance_start)
            history_account.append(data_temporary)
            data_temporary = []

        elif data_input[0] == "magazyn":
            for key in product_dict:
#                print(f"{key} {product_dict[key]}")
                data_temporary.append("magazyn")
                data_temporary.append(key)
                data_temporary.append(product_dict[key])
                history_account.append(data_temporary)
                data_temporary = []

        elif data_input[0] == "przeglad":
#            print(f"{history_account}")
            data_temporary.append("przeglad")
            data_temporary.append(history_account)
            history_account.append(data_temporary)
            data_temporary = []

        elif data_input[0] == "stop":
            history_account.append(data_input)
            break

        else:
            print("ERROR")
#    print(history_account)
    return history_account


running_process()

# "writing to file all history of accounting process"
# with open("out.txt", "w") as file:
#     for i in history_account:
#         for element in i:
#             file.write(element + "\n")

#    print(colored(f"product_dict: {product_dict}", "yellow"))
#    print(colored(f"balance_start: {balance_start}", "yellow"))
#    print(colored(f"history_account: {history_account}", "yellow"))
#    print("-" * 100)




