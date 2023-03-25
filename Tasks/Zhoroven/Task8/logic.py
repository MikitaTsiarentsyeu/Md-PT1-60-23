class ValidationUser:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    name = property(get_name)
    email = property(get_email)


def view_menu():
    try:
        with open('Menu.txt', 'r', encoding='utf-8') as m:
            return m.read()
    except FileNotFoundError:
        return file_error()


def search_sushi(search):
    try:
        with open('Menu.txt', 'r', encoding='utf-8') as m:
            res = [line.strip()
                   for line in m if search.lower() in line.lower()]
        return '\n'.join(res)
    except FileNotFoundError:
        return file_error()


def file_error():
    return f"File not found!"


def add_info(name, email):
    with open('data.txt', 'a') as d:
        entry = ValidationUser(name, email)
        d.write(f"[{entry.name} {entry.email}]\n")
