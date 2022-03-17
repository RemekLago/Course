import json
import csv
import os.path
import pickle
import sys

# x = sys.argv
x = ["lesson_6_reader.py", "TestDict/bazatest.csv", "TestDict/TestDict4/bazatest4.json", "1,1,2", "2,2,6"]
changes = x[3:]


class CommandData:
    def __init__(self, src, dst, changes, input_type=None, output_type=None):
        self.src = src
        self.dst = dst
        self.changes = changes
        self.input_type = input_type
        self.output_type = output_type


    def file_csv_read(self, src):
        with open(src, "r") as file:
            reader = csv.reader(file)
        return reader

    def file_json_read(self, src):
        with open(src, "r") as file:
            reader = json.load(file)
        return reader

    def file_pickle_read(self, src):
        with open(src, "rb") as file:
            reader = pickle.load(file)
        return reader

    def changes_in_file(self, changes, file_to_edit):
        for idx in changes:
            file_to_edit[idx[0]][idx[1]] = idx[2]
        return file_to_edit

    def file_csv_write(self, dst):
        writer = file_with_changes
        with open(dst, "w") as file:
            writer = csv.writer(file)
            writer.writerows(list_csv)

    def file_json_write(self, dst):
        writer = file_with_changes
        with open(dst, "w") as file:
            json.dump(writer, file)

    def file_pickle_write(self, dst):
        writer = file_with_changes
        with open(dst, "wb") as file:
            pickle.dump(writer, file)

command = CommandData(x[1], x[2], x[3], x[4])

def type_of_input_file():
    # path = sys.argv[1]
    path = x[1]
    type_file = None
    file = os.path.split(path)
    if file[1].endswith(".json"):
        type_file = "json"
    elif file[1].endswith(".csv"):
        type_file = "csv"
    elif file[1].endswith(".pickle"):
        type_file = "pickle"
    else:
        print("ERROR, given file extension isn't json, csv or pickle")
    command.input_type = type_file
    return command.input_type

def type_of_output_file():
    # path = sys.argv[2]
    path = x[2]
    type_file = None
    file = os.path.split(path)
    if file[1].endswith(".json"):
        type_file = "json"
    elif file[1].endswith(".csv"):
        type_file = "csv"
    elif file[1].endswith(".pickle"):
        type_file = "pickle"
    else:
        print("ERROR, given file extension isn't json, csv or pickle")
    command.output_type = type_file
    return command.output_type

def is_source_path_exist():
    path = os.path.exists(command.src)
    if path:
        return True
    else:
        print("ERROR, given path doesn't exist")

def is_destination_path_exist():
    path_folder = os.path.split(command.dst)
    path = os.path.exists(path_folder[1])
    if not path:
        os.makedirs(path_folder[1])

def take_reader_to_edit()
    source = is_source_path_exist()
    type_input = type_of_input_file()
    if type_input == "csv" and source:
        file_to_edit = command.file_csv_read(x[1])
    elif type_input == "json" and source:
        file_to_edit = command.file_json_read(x[1])
    elif type_input == "pickle" and source:
        file_to_edit = command.file_pickle_read(x[1])
    return file_to_edit

def take_file_to_write():
    type_output = type_of_output_file()
    if type_output == "csv":
        command.file_csv_write(x[1])
    elif type_output == "json":
        command.file_json_write(x[1])
    elif type_output == "pickle":
        command.file_pickle_write(x[1])

def final():
    is_destination_path_exist()
    type_of_input_file()
    type_of_output_file()
    file_to_edit = take_reader_to_edit()
    command.changes_in_file(changes, file_to_edit)
    take_file_to_write()







