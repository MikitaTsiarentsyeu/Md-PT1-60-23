import csv
import sys


class Bracelet:
    def __init__(self, material, color, size, sex):
        self.__material = material
        self.__color = color
        self.__size = size
        self.__sex = sex

    def add_new_bracelet(self):
        with open("file.csv", 'a', newline='\n') as f:
            writer = csv.writer(f)
            writer.writerow([self.__material, self.__color, self.__size, self.__sex])


def quit():
    return sys.exit()


# def get_all_bracelets():
#     try:
#         with open("file.csv", 'r') as f:
#             reader = csv.DictReader(f)
#             l = [[(key + ': ' + value) for key, value in row.items()]
#                  for row in reader]
#             return '\n'.join([', '.join([y for y in x]) for x in l])
#     except FileNotFoundError:
#         return False


def search(param, value):
    try:
        with open("file.csv", 'r') as f:
            reader = csv.DictReader(f)
            if param:
                l = [[(key + ': ' + values) for key, values in row.items()
                      if row[param] == value] for row in reader]
            else:
                l = [[(key + ': ' + value) for key, value in row.items()]
                     for row in reader]
            return '\n'.join([', '.join([y for y in x]) for x in l if x])
    except FileNotFoundError:
        return False
