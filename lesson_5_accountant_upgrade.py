import sys
from input_5_accountant_upgrade import check_kind_of_input as command_final

history_account = []
balance_start = 0
product_dict = {}
command_final = command_final()

"""add a task from input to the previous history updated from file in2.txt
remove command stop and than add it on the end of list"""
command_stop = ["stop"]
command_final.remove(command_stop)
new_command_input = sys.argv
command_final.append(new_command_input[2:])
command_final.append(command_stop)
command_output_file = new_command_input[1]

# print(command_final)

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
        list_temporary = []
        # print(f"{balance_start}")
        list_temporary.append(data_input[0])
        list_temporary.append(balance_start)
        history_account.append(list_temporary)

    elif data_input[0] == "magazyn":
        list_temporary = []
        for key in product_dict:
            # print(f"{key} {product_dict[key]}")
            list_temporary.append(data_input[0])
            list_temporary.append(key)
            list_temporary.append(product_dict[key])
            history_account.append(list_temporary)

    elif data_input[0] == "przeglad":
        list_temporary = []
        # print(f"{history_account}")
        list_temporary.append(data_input[0])
        list_temporary.append(history_account)
        history_account.append(list_temporary)
        continue

    elif data_input[0] == "stop":
        history_account.append(data_input)
        break

    # else:
    #     print("ERROR")

# """writing to file all history of accounting process"""
# with open("out.txt", "w") as file:
#     for i in history_account:
#         for element in i:
#             file.write(element + "\n")
