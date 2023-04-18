import csv
import sys
import datetime

keys_data = ['Product', 'Country', 'Variety', 'Caliber', 'Price']


def exit():
    return sys.exit()


def add_new_product(lst):
    week = str(datetime.datetime.now().isocalendar().week)
    week = [week]
    data_product = week + lst

    with open('fruit.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data_product)


def search_key_value(key, value):
    with open('fruit.csv', 'r') as f:
        reader = csv.DictReader(f)
        lst = [row for row in reader if row[key] == value]
        out = [[values for key, values in row.items()] for row in lst]
        return '\n'.join(['|'.join([x for x in i]) for i in out]) 
    
def search_key(x):
    with open('fruit.csv', 'r') as f:
        reader = csv.DictReader(f)
        lst = [row for row in reader]
        out = [[values for key, values in row.items() if key == x] for row in lst]
        return out


def get_all():
    with open('fruit.csv', 'r') as f:
        reader = csv.DictReader(f)
        lst = [row for row in reader]
        out = [[values for key, values in row.items()] for row in lst]
        return '\n'.join(['|'.join([x for x in i]) for i in out])
