from lesson_5_accountant_upgrade import history_account as data
from lesson_5_accountant_upgrade import command_output_file \
    as command_output_file


class DataAccountant:
    def __init__(self, magazyn):
        self.magazyn = magazyn


def writing_data():
    input_data = data
    for idx in input_data:
        if idx[0] == "magazyn":
            record = DataAccountant(idx[0])
            with open(f'{command_output_file}', "a") as file:
                file.write(record.magazyn + "\n")


writing_data()