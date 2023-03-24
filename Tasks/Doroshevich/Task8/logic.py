import csv
import sys


class BraceletAdd:
    def __init__(self, material, color, size, sex, price):
        self.__material = material
        self.__color = color
        self.__size = size
        self.__sex = sex
        self.__price = price

    def get_material(self):
        return self.__material

    def get_color(self):
        return self.__color

    def get_size(self):
        return self.__size

    def get_sex(self):
        return self.__sex
    
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        self.__price = price
    
    material = property(get_material)
    color = property(get_color)
    size = property(get_size)
    sex = property(get_sex)
    price = property(get_price, set_price)

    def add_new_bracelet(self):
        try:
            with open("file.csv") as bracelets:
                reader = csv.DictReader(bracelets)
                for row in reader:
                    last_index = int(row['index'])
                with open("file.csv", 'a', newline='\n') as f:
                    writer = csv.writer(f)
                    writer.writerow([str(last_index + 1), self.material, self.color, self.size, self.sex, self.price])
        except FileNotFoundError:
            with open("file.csv", 'w', newline='\n') as f:
                    writer = csv.writer(f)
                    writer.writerow(['index','material','color', 'size', 'sex', 'price'])
                    writer.writerow(['1' , self.material, self.color, self.size, self.sex, self.price])


class BraceletManage:

    def __init__(self):
        self.__output = []

    def search(self, param, value):
        try:
            with open("file.csv", 'r') as f:
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
    
    def index_proof(self, index):
            with open("file.csv") as f:
                reader = csv.DictReader(f)
                return index in [row['index'] for row in reader]

    def delete_bracelet(self, index):
        with open("file.csv") as f:
            reader = csv.DictReader(f)
            data = [row for row in reader if row['index'] != index]
            keys = list(data[0].keys())
            values = [list(x.values())[1:] for x in data]
            l = []
            i = 1
            for x in values:
                l.append([i] + x)
                i += 1
        BraceletManage().build_file(keys, l)

    def change_price(self, index, new_price):
        with open("file.csv") as f:
            reader = csv.DictReader(f)
            data = []
            for row in reader:
                if row['index'] == index:
                    row['price'] = new_price
                data.append(row)
            keys = list(data[0].keys())
            values = [list(x.values()) for x in data]
        BraceletManage().build_file(keys, values)
    
    def discount(self, switch, discount):
        with open("file.csv") as f:
            reader = csv.DictReader(f)
            data = []
            for row in reader:
                if switch:
                    row['price'] = str(round(float(row['price']) * (100 - discount) / 100, 2))
                else:
                    row['price'] = str(round(float(row['price']) / ((100 - discount) / 100), 2))
                data.append(row)
            keys = list(data[0].keys())
            values = [list(x.values()) for x in data]
        BraceletManage().build_file(keys, values)

    
    def build_file(self, keys, values):
        with open("file.csv", 'w', newline='\n') as f:
            writer = csv.writer(f)
            writer.writerow(keys)
            for x in values:
                writer.writerow(x)


    

def quit():
    return sys.exit()