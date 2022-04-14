from lesson_5_accountant_upgrade import history_account as data
from lesson_5_accountant_upgrade import command_output_file \
    as command_output_file

class DataAccountant:
    def __init__(self, saldo, balance, comment):
        self.saldo = saldo
        self.balance = balance
        self.comment = comment


def writing_data():
    input_data = data
    for idx in input_data:
        if idx[0] == "saldo":
            record = DataAccountant(idx[0], idx[1], idx[2])
            with open(f'{command_output_file}', "a") as file:
                file.write(record.saldo + "\n")
                file.write(record.balance + "\n")
                file.write(record.comment + "\n")

writing_data()