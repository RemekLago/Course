from lesson_3_accountant_upgrade import running_process

data = running_process()


class DataAccountant:
    def __init__(self, saldo, balance, comment):
        self.saldo = saldo
        self.balance = balance
        self.comment = comment

    def writing_to_file(self, record):
        with open("out_saldo.txt", "a") as file:
            file.write(record.saldo + "\n")
            file.write(record.balance + "\n")
            file.write(record.comment + "\n")


def writing_data():
    input_data = data
    for idx in input_data:
        if idx[0] == "saldo":
            command = DataAccountant(idx[0], idx[1], idx[2])
            command.writing_to_file(command)


writing_data()






