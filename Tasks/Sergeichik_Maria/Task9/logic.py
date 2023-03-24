import csv

FILENAME = "C:/Users/Acer/Documents/GitHub/Md-PT1-60-23/Tasks/Sergeichik_Maria/Task8/films.csv"

class Film:
    def __init__(self, name, producer, year, genre):
        self.__name = name
        self.__producer = producer
        self.__year = year
        self.__genre = genre
    def alls(self):
         print(self.__name + "," + self.__producer + "," + self.__year + "," + self.__genre)
    def get_name(self):
        return self.__name   
    def refreshData(self, producer, year, genre):
        self.__producer = producer
        self.__year = year
        self.__genre = genre
          

films = [Film("The Disgusting Eight", "Quentin Tarantino", "2015", "Drama")]
nameKey = "name"
producerKey = "producer"
yearKey = "year"
genreKey = "genre"


def add_film(name, producer, year, genre):

    isFound = False
    
    

    for i in films:
        if str(i.get_name) == str(name):
            i.refreshData(producer, year, genre)
            isFound = True

    if isFound == False:
        films.append (Film(name, producer, year, genre))
            


def get_all_films():

    for i in films:
        i.alls()
    
    

def get_record_by_name(name):
    try:
        for i in films:
            if str(i.get_name) == str(name):
                i.alls()
             
    except KeyError:
        print("Dont found")