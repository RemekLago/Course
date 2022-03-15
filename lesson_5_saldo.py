from lesson_3_accountant_upgrade import history_account as data


class DataAccountant:
    def __init__(self, saldo, balance, comment):
        self.saldo = saldo
        self.balance = balance
        self.comment = comment


def writing_data():
    input_data = data
    for idx in input_data:
        if idx[0] == "saldo.py":
            record = DataAccountant(idx[1], idx[2], idx[3])
            with open("out_saldo.txt", "a") as file:
                file.write(record.saldo + "\n")
                file.write(record.balance + "\n")
                file.write(record.comment + "\n")


print(data)
writing_data()






