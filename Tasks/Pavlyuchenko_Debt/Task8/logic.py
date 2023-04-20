import csv
import sys

def exit():
    return sys.exit()

class PriceAdd:
    def __init__(product, country, variety, caliber, price):
        self.__product = product
        self.__country = country
        self.__variety = variety
        self.__caliber = caliber
        self.__price = price

    def get_product(self):
        return self.__product

    def get_counry(self):
        return self.__country

    def get_variety(self):
        return self.__variety

    def get_caliber(self):
        return self.__caliber
    
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        self.__price = price
    
    product = property(get_product)
    country = property(get_country)
    variety = property(get_variety)
    caliber = property(get_caliber)
    price = property(get_price, set_price)

    def add_new_product(self):
        try:
            with open("fruit.csv") as product:
                reader = csv.DictReader(product)
                for row in reader:
                    last_index = int(row['index'])
                with open("fruit.csv", 'a', newline='\n') as f:
                    writer = csv.writer(f)
                    writer.writerow([str(last_index + 1), self.product, self.country, self.variety, self.caliber, self.price])
        except FileNotFoundError:
            with open("file.csv", 'w', newline='\n') as f:
                    writer = csv.writer(f)
                    writer.writerow('Index', 'Product', 'Country', 'Variety', 'Caliber', 'Price'])
                    writer.writerow(['1' , self.product, self.country, self.variety, self.caliber, self.price])



class ProductManage:
    def __init__(self):
        self.__output = []

    def delete_product(self, index):
        with open("fruit.csv") as f:
            reader = csv.DictReader(f)
            data = [row for row in reader if row['index'] != index]
            keys = list(data[0].keys())
            values = [list(x.values())[1:] for x in data]
            l = []
            i = 1
            for x in values:
                l.append([i] + x)
                i += 1
        ProductManage().build_file(keys, l)

    def change_price(self, index, new_price):
        with open("fruit.csv") as f:
            reader = csv.DictReader(f)
            data = []
            for row in reader:
                if row['index'] == index:
                    row['price'] = new_price
                data.append(row)
            keys = list(data[0].keys())
            values = [list(x.values()) for x in data]
        ProductManage().build_file(keys, values)

    def search(self, param, value):
        try:
            with open("fruit.csv", 'r') as f:
                reader = csv.DictReader(f)
                if param and isinstance(value, str):
                    self.__output = [[(key + ': ' + value) for key, value in row.items()]
                    for row in reader if row[param] == value]
                elif param and isinstance(value, list):
                    self.__output = [[(key + ': ' + value) for key, value in row.items()]
                    for row in reader if value[0] <= float(row[param]) <= value [1]]
                else:
                    self.__output = [[(key + ': ' + value) for key, value in row.items()]
                    for row in reader]
                return '\n'.join([', '.join([y for y in x]) for x in self.__output])
        except FileNotFoundError:
            return False

    def build_file(self, keys, values):
        with open("fruit.csv", 'w', newline='\n') as f:
            writer = csv.writer(f)
            writer.writerow(keys)
            for x in values:
                writer.writerow(x)
