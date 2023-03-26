import uuid

class PhoneBookEntry:

    def __init__(self, name):
        self.__id = uuid.uuid4()
        self.__name = name
        self.__numbers = []

    def get_id(self):
        return self.__id
    
    def get_name(self): 
        return self.__name

    def set_name(self, name):
        self.__name = name

    id = property(get_id)
    name = property(get_name, set_name)

    # def add_number(self, number):
    #     if number not in self.__numbers:
    #         self.__numbers.append(number)

    def add_numbers(self, *numbers):
        for number in numbers:
            if number not in self.__numbers:
                self.__numbers.append(number)


    def remove_numbers(self, *numbers):
        for number in numbers:
            i = self.__numbers.index(number)
            if i >= 0:
                del self.__numbers[i]

            
    def clear_numbers(self):
        self.__numbers = []

    
    def __str__(self):
        return f"{self.name}:{','.join(self.__numbers)}"
    

class PhooneBookManager:

    def __init__(self):
        self.__repo = []

    def get_all_records(self):
        return '\n'.join([str(e) for e in self.__repo])

    def get_record_by_name(self, name):
        res = [entry for entry in self.__repo if entry.name == name]
        return '\n'.join(str(e) for e in self.__repo)

    def add_record(self, name, numbers):
        entry = PhoneBookEntry(name)
        entry.add_numbers(*numbers)
        self.__repo.append(entry)

if __name__ == "__main__":


    
    entry = PhoneBookEntry("test name")
    entry.add_numbers("1234567", "7654321")
    print(entry)
    print(entry.id)