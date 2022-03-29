import json
import csv
import os.path
import pickle
import sys

# x = sys.argv
x = ["lesson_6_reader.py", "TestDict/bazatest.csv",
     "TestDict/TestDict1/bazatest5.json", "1,1,2", "1,1,6"]
changes = [[int(idy) for idy in idx.split(",")] for idx in x[3:]]


class CommandData:
    def __init__(self, src, dst, changes):
        self.src = src
        self.dst = dst
        self.changes = changes
        self.input_type = self.type_of_file(src)
        self.output_type = self.type_of_file(dst)
        self.source_path_exist = self.is_source_path_exist()
        self.destination_path_exist = self.is_destination_path_exist()

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

    def print_changes(self, file):
        for _ in file:
            print(_)

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
        type_file = None
        if path.endswith(".json"):
            type_file = "json"
        elif path.endswith(".csv"):
            type_file = "csv"
        elif path.endswith(".pickle"):
            type_file = "pickle"
        else:
            print("ERROR, given file extension isn't json, csv or pickle")
        return type_file

    def is_source_path_exist(self):
        path = os.path.exists(self.src)
        if path:
            return True
        else:
            print("ERROR, given path doesn't exist")

    def is_destination_path_exist(self):
        path_folder = os.path.split(self.dst)
        path = os.path.exists(path_folder[0])
        if not path:
            os.makedirs(path_folder[0])

    def process(self):
        self.is_source_path_exist()
        self.is_destination_path_exist()
        if self.input_type == "csv":
            content = self.file_csv_read()
        elif self.input_type == "json":
            content = self.file_json_read()
        elif self.input_type == "pickle":
            content = self.file_pickle_read()
        content = self.changes_in_file(content)
        self.print_changes(content)
        if self.output_type == "csv":
            self.file_csv_write(content)
        elif self.output_type == "json":
            self.file_json_write(content)
        elif self.output_type == "pickle":
            self.file_pickle_write(content)


command = CommandData(x[1], x[2], changes)

command.process()







