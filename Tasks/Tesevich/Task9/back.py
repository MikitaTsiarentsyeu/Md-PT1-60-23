import json
import uuid
class Films:
    def __init__(self, film, autor, year, genre):
        self.__all_in = []
        self.__id = str(uuid.uuid4())
        self.__film = film
        self.__autor = autor
        self.__year = year
        self.__genre = genre
    
    def get_all_in(self):
        return self.__all_in  
      
    def get_film(self):
        return self.__film
    def set_film(self, film):
        self.__film = film

    def get_autor(self):
        return self.__autor
    def set_autor(self, autor):
        self.__autor = autor
    
    def get_year(self):
        return self.__year
    def set_year(self, year):
        self.__year = year
    
    def get_genre(self):
        return self.__genre
    def set_genre(self, genre):
        self.__genre = genre
    
    def get_id(self):
        return self.__id
        

    film = property(get_film, set_film)
    autor = property(get_autor, set_autor)
    year = property(get_year, set_year)
    genre = property (get_genre, set_genre)
    id= property(get_id)
    
    def data_writer(self):
        with open ('storage_films.json', 'r') as storage_can:
            storage = json.load(storage_can)
            storage.append({self.id:{'film':self.film,'autor':self.autor,'year':self.year,'genre':self.genre}})
        with open ('storage_films.json', 'w') as storage_can:
            json.dump(storage,storage_can,indent='\t')

    def data_reader():
        with open ('storage_films.json', 'r') as storage_can:
            rez = []
            storage = json.load(storage_can)
            for i in storage:
                i = i.values()
                for i in i:
                    rez.append(i)
            return rez
                
    def search(serch,by_what):
        rez=[]
        data = Films.data_reader()
        for i in data:
            if (i.get(by_what).find(serch))>-1:
                rez.append(i)
        return rez
 

               
#print(Films.data_reader())