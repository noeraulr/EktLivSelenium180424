import pickle
import csv


def create_NestedListFile_01():
    with open("THD260324.csv", "r", encoding='utf-8') as read_obj:
        csv_reader = csv.reader(read_obj)
        # print(csv_reader)
        nested_list = list(csv_reader)
    file_path = "THD260324_01.py"
    with open(file_path, "w") as file:
        file.write("nested_list = " + repr(nested_list))
        # file.write( repr(nested_list))
        # file.write("\n")


if __name__ == '__main__':
    print(create_NestedListFile_01())
