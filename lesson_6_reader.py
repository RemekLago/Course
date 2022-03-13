import json
import csv
import os.path
import pickle
import sys

# x = sys.argv
x = ["TestDict/TestDict2/testfile3.csv", "TestDict/TestDict4/", 1, 2]


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
        list_json = []
        with open(src, "r") as file:
            reader = json.loads(file)
            for row in reader:
                list_json.append(row)
        list_json[change1][change2] = value

        with open(dst, "w") as file:
            writer = json.dumps(file)
            writer.writerows(list_json)


    def file_pickle_read_write(self, src, dst, change1, change2, value):
        list_pickle = []
        with open(src, "rb") as file:
            reader = pickle.loads(file)
            for row in reader:
                list_pickle.append(row)
        list_pickle[change1][change2] = value

        with open(dst, "wb") as file:
            writer = pickle.dumps(file)
            writer.writerows(list_pickle)


input_command = InputData(x[0], x[1], x[2], x[3])


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
    path = os.path.exists(input_command.dst)
    # print(path)
    if not path:
        os.makedirs(input_command.dst)


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




