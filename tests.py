import sys

balance_start = 10000
product_dict = {}
quantity_start_1 = 0
quantity_start_2 = 0
quantity_start_3 = 0
history_account = []
i = 1

for i in range(1):
    data_input = sys.argv
    if data_input[1] == "saldo":
        balance = int(data_input[2])
        comment = data_input[3]
        history_account.append(data_input)
        balance_start += balance

    elif data_input[1] == "zakup":
        product_id = data_input[2]
        price = int(data_input[3])
        quantity = int(data_input[4])
        balance_start -= price * quantity
        if product_id == "product1":
            quantity_start_1 += quantity
        if product_id == "product2":
            quantity_start_2 += quantity
        if product_id == "product3":
            quantity_start_3 += quantity
        if balance_start < 0:
            print("ERROR - balance lower than 0")
        if price < 0:
            print("ERROR - price lower than 0")
        if quantity < 0:
            print("ERROR - quantity lower than 0")
        history_account.append(data_input)
    elif data_input[1] == "sprzedaz":
        product_id = data_input[2]
        price = int(data_input[3])
        quantity = int(data_input[4])
        balance_start += price * quantity
        if product_id == "product1":
            if quantity_start_1 >= quantity:
                quantity_start_1 -= quantity
            else:
                print("ERROR - quantity after sale lower than 0")
        if product_id == "product2":
            if quantity_start_2 >= quantity:
                quantity_start_2 -= quantity
            else:
                print("ERROR - quantity after sale lower than 0")
        if product_id == "product3":
            if quantity_start_3 >= quantity:
                quantity_start_3 -= quantity
            else:
                print("ERROR - quantity after sale lower than 0")
        if price < 0:
            print("ERROR - price lower than 0")
        if quantity < 0:
            print("ERROR - quantity lower than 0")
        history_account.append(data_input)
    elif data_input[1] == "konto":
        pass
        history_account.append(data_input)

    elif data_input[1] == "magazyn":
        product_id_list = []
        for idx in range(2, len(data_input)):
            product_id_list.append(data_input[idx])
        history_account.append(data_input)

    elif data_input[1] == "przeglad":
        pass
        history_account.append(data_input)

    elif data_input[1] == "stop":
        pass
        history_account.append(data_input)

    else:
        print("ERROR")
        history_account.append(data_input)

    print(f"balance_start: {balance_start}")
    print(f"ID product1 quantity: {quantity_start_1}")
    print(f"ID product2 quantity: {quantity_start_2}")
    print(f"ID product3 quantity: {quantity_start_3}")
    print(f"history_account: {history_account}")

