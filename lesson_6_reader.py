import json
import csv
import os.path
import pickle
import sys

# x = sys.argv
x = ["TestDict/bazatest.csv", "TestDict/TestDict5/bazatest2.csv", 1, 2, 6]


class InputData:
    def __init__(self, src, dst, change1, change2, value, type=None):
        self.src = src
        self.dst = dst
        self.change1 = change1
        self.change2 = change2
        self.value = value
        self.type = type

    def file_csv_read_write(self, src, dst, change1, change2, value):
        list_csv = []
        with open(src, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                list_csv.append(row)
        list_csv[change1][change2] = value
        with open(dst, "w") as file:
            writer = csv.writer(file)
            writer.writerows(list_csv)

    def file_json_read_write(self, src, dst, change1, change2, value):
        with open(src, "r") as file:
            list_json = json.load(file)
            list_json[change1][change2] = value

        with open(dst, "w") as file:
            json.dump(list_json, file)

    def file_pickle_read_write(self, src, dst, change1, change2, value):
        with open(src, "rb") as file:
            list_pickle = pickle.load(file)
            list_pickle[change1][change2] = value

        with open(dst, "wb") as file:
            pickle.dump(list_pickle, file)


input_command = InputData(x[0], x[1], x[2], x[3], x[4])


def type_of_input_file():
    # path = sys.argv[0]
    path = x[0]
    type_file = None
    file = os.path.split(path)
    if file[1].endswith(".json"):
        type_file = "json"
    elif file[1].endswith(".csv"):
        type_file = "csv"
    elif file[1].endswith(".pickle"):
        type_file = "pickle"
    # print(type_file)
    else:
        print("ERROR, given file extension isn't json, csv or pickle")
    input_command.type = type_file
    return type_file


def is_source_path_exist():
    path = os.path.exists(input_command.src)
    if path:
        return True
    else:
        print("ERROR, given path doesn't exist")


def is_destination_path_exist():
    path_folder = os.path.split(input_command.dst)
    path = os.path.exists(path_folder[0])

    if not path:
        os.makedirs(path_folder[0])


def final():
    is_source_path_exist()
    is_destination_path_exist()
    type_input = type_of_input_file()
    if type_input == "csv":
        input_command.file_csv_read_write()
    elif type_input == "json":
        input_command.file_json_read_write()
    elif type_input == "pickle":
        input_command.file_pickle_read_write()