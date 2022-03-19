import json
import csv
import os.path
import pickle
import sys

# x = sys.argv
x = ["lesson_6_reader.py", "TestDict/bazatest.csv", "TestDict/TestDict4/bazatest4.json", "1,1,2", "1,2,6"]
changes = [[int(idy) for idy in idx.split(",")] for idx in x[3:]]
print(changes)

class CommandData:
    def __init__(self, src, dst, changes):
        self.src = src
        self.dst = dst
        self.changes = changes
        self.input_type = self.type_of_file(src)
        self.output_type = self.type_of_file(dst)


    def file_csv_read(self):
        with open(self.src, "r") as file:
            reader = csv.reader(file)
            content = [row for row in reader]
        return content

    def file_json_read(self):
        with open(self.src, "r") as file:
            content = json.load(file)
        return content

    def file_pickle_read(self):
        with open(self.src, "rb") as file:
            content = pickle.load(file)
        return content

    def changes_in_file(self, file_to_edit):
        for idx in self.changes:
            file_to_edit[idx[0]][idx[1]] = idx[2]
        return file_to_edit

    def file_csv_write(self, file_with_changes):
        with open(self.dst, "w") as file:
            writer = csv.writer(file)
            writer.writerows(file_with_changes)

    def file_json_write(self, file_with_changes):
        with open(self.dst, "w") as file:
            json.dump(file_with_changes, file)

    def file_pickle_write(self, file_with_changes):
        with open(self.dst, "wb") as file:
            pickle.dump(file_with_changes, file)

    def type_of_file(self, path):
        # path = sys.argv[1]
        type_file = None
        if path.endswith(".json"):
            # type_of_file = json
            type_file = "json"
        elif path.endswith(".csv"):
            type_file = "csv"
        elif path.endswith(".pickle"):
            type_file = "pickle"
        else:
            print("ERROR, given file extension isn't json, csv or pickle")
        return type_file

    def process(self):
        if self.input_type == "csv":
            content = self.file_csv_read()
        elif self.input_type == "json":
            content = self.file_json_read()
        elif self.input_type == "pickle":
            content = self.file_pickle_read()
        content = self.changes_in_file(content)
        if self.output_type == "csv":
            self.file_csv_write(content)
        elif self.output_type == "json":
            self.file_json_write(content)
        elif self.output_type == "pickle":
            self.file_pickle_write(content)


command = CommandData(x[1], x[2], changes)

command.process()


#
# def is_source_path_exist(src):
#     path = os.path.exists(src)
#     if path:
#         return True
#     else:
#         print("ERROR, given path doesn't exist")
#
#
# def is_destination_path_exist(dst):
#     path_folder = os.path.split(dst)
#     path = os.path.exists(path_folder[1])
#     if not path:
#         os.makedirs(path_folder[1])
#
#
# def take_reader_to_edit():
#     source = is_source_path_exist()
#     type_input = type_of_input_file()
#     if type_input == "csv" and source:
#         file_to_edit = command.file_csv_read(x[1])
#     elif type_input == "json" and source:
#         file_to_edit = command.file_json_read(x[1])
#     elif type_input == "pickle" and source:
#         file_to_edit = command.file_pickle_read(x[1])
#     return file_to_edit
#
# def take_file_to_write():
#     type_output = type_of_output_file()
#     if type_output == "csv":
#         command.file_csv_write(x[1])
#     elif type_output == "json":
#         command.file_json_write(x[1])
#     elif type_output == "pickle":
#         command.file_pickle_write(x[1])
#
# def final():
#     is_destination_path_exist()
#     # type_of_input_file()
#     type_of_output_file()
#     file_to_edit = take_reader_to_edit()
#     command.changes_in_file(changes, file_to_edit)
#     take_file_to_write()
#
# # final()







