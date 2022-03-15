from lesson_5_accountant_upgrade import history_account as data
from lesson_5_accountant_upgrade import command_output_file \
    as command_output_file


class DataAccountant:
    def __init__(self, zakup, product_id, price, quantity):
        self.zakup = zakup
        self.product_id = product_id
        self.price = price
        self.quantity = quantity


def writing_data():
    input_data = data
    for idx in input_data:
        if idx[0] == "zakup":
            record = DataAccountant(idx[1], idx[2], idx[3], idx[4])
            with open(f'{command_output_file}', "a") as file:
                file.write(record.zakup + "\n")
                file.write(record.product_id + "\n")
                file.write(record.price + "\n")
                file.write(record.quantity + "\n")

writing_data()






