import json

class Movie:
    def __init__(self, title, director, year, genre):
        self.__title = title
        self.__director = director
        self.__year = year
        self.__genre = genre

    def get_title(self):
        return self.__title
    
    def get_year(self):
        return self.__year
    
    def get_genre(self):
        return self.__genre

    def get_all(self):
        new_entry = {"title": self.__title, "director": self.__director, 
        "year": self.__year, "genre": self.__genre}
        return new_entry

    def get_movie(self):
        result = [self.__title, self.__director, 
        self.__year, self.__genre]
        return result

    def choise_key(self, key):
        if key == 'title':
            return self.get_title()
        elif key == 'year':
            return self.get_year()
        elif key == 'genre':
            return self.get_genre()



try:
    with open('movies.json', 'r') as f:
        new_file = json.load(f)
except(FileNotFoundError, json.decoder.JSONDecodeError):
    new_file = []

instances_list = []
for dic in new_file:   
    instances_list.append(Movie(dic['title'],dic['director'],dic['year'],dic['genre']))

def all_movies():
    new_list = []
    for item in instances_list:
        new_list.append(item.get_all())
    return new_list

def search_movie(name, key):
    new_list = []
    for item in instances_list:
        if item.choise_key(key) == name:
            new_list.append(item.get_movie())
    return new_list


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
