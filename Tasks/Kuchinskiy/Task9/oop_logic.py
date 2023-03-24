import json
# в этом файле треним разные способы написания классов, 
# поэтому функционал программы 
# может осуществляться разными способами
# 1) поиск фильмов и возврат всех фильмов осуществляется через classmethod
# 2) запись: используем объект класса и добавляем в файл
# 3) удаление: создание объектов класса используя данные из файла
class Movie:
    try: # создаем атрибут класса, чтобы работать с ним в рамках класса
        with open('movies.json', 'r') as f:
            new_file = json.load(f)
    except(FileNotFoundError, json.decoder.JSONDecodeError):
        new_file = []

    @classmethod # поиск фильмов
    def search_movie(cls, name, keys):
        output = []
        for dic in cls.new_file:
            if dic[keys] == name:
                output.append([val for val in dic.values()])
        return output

    @classmethod # вернуть все фильмы
    def get_all_movies(cls):
        output = []
        for dic in cls.new_file:
            output.append([val for val in dic.values()])
        return output
            

    def __init__(self, title, director, year, genre):
        self.__title = title
        self.__director = director
        self.__year = year
        self.__genre = genre

    def get_all(self): # возвращает инфу для записи в файл
        new_entry = {"title": self.__title, "director": self.__director, 
        "year": self.__year, "genre": self.__genre}
        return new_entry

    def get_title(self):
        return self.__title

    all = property(get_all)


try:
    with open('movies.json', 'r') as f:
        new_file = json.load(f)
except(FileNotFoundError, json.decoder.JSONDecodeError):
    new_file = []

instances_list = []
for dic in new_file:   
    instances_list.append(Movie(dic['title'],dic['director'],dic['year'],dic['genre']))


def write_back(func): # декоратор для записи после удаления
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        new_file_after_del = []
        for inst in instances_list:
            new_file_after_del.append(inst.get_all())
        with open('movies.json', 'w') as f:
            json.dump(new_file_after_del, f, indent=3)
    return inner

@write_back
def del_film(name): # функция удаления
    for inst in instances_list:
        if inst.get_title() == name:
            instances_list.remove(inst)


def add_new_film(*args):
    new_movie = Movie(*args)
    if new_movie.get_all() not in new_file:
        new_file.append(new_movie.get_all())
    with open('movies.json', 'w') as f:
        json.dump(new_file, f, indent=3)
