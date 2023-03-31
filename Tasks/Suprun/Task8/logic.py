import csv
class Movies:
    def __init__(self, title, director, year, genre):
        self.__title = title
        self.__director = director
        self.__year = year
        self.__genre = genre

    def get_titel(self):
        return self.__title
    def set_titel(self, title):
        self.__title = title
        
    def get_director(self):
        return self.__director
    def set_director(self, director):
        self.__director = director
    
    def get_year(self):
        return self.__year
    def set_year(self, year):
        self.__year = year
    
    def get_genre(self):
        return self.__genre
    def set_genre(self, genre):
        self.__genre = genre
    
    title = property(get_titel, set_titel)
    director = property(get_director, set_director)
    year = property(get_year, set_year)
    genre = property(get_genre, set_year)

def add_a_new_movie(title, director, year, genre):
    dict_temp = {}
    movie = Movies(title, director, year, genre)
    dict_temp['title'] = movie.title
    dict_temp['director'] = movie.director
    dict_temp['year'] = movie.year
    dict_temp['genre'] = movie.genre
    with open("store.csv",'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(dict_temp.values())

def get_all_movies():
    with open("store.csv", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield (f"title: {row['title']}, director: {row['director']}, year: {row['year']}, genre: {row['genre']}")
       

def search(item):
     with open("store.csv", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if item in row.values():
                yield(f"title: {row['title']}, director: {row['director']}, year: {row['year']}, genre: {row['genre']}")
            


