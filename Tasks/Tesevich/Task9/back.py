import json

class Films:
    def __init__(self, film, autor, year, genre):
        self.__film = film
        self.__autor = autor
        self.__year = year
        self.__genre = genre
    
    def get_film(self):
        return self.__film
    def set_film(self, film):
        self.__film = film

    def get_autor(self):
        return self.__autor  
    def set_autor(self, autor):
        self.__film = autor

    def get_year(self):
        return self.__year   
    def set_year(self, year):
        self.__film = year

    def get_genre(self):
        return self.__genre  
    def set_genre(self, genre):
        self.__film = genre

    

    film = property(get_film, get_film)
    autor = property(get_autor,set_autor)
    year = property(get_year, set_year)
    genre = property (get_genre,set_genre)
    def do_big(self):
        return {"film":self.film, "autor":self.autor, "year":self.year, "genre":self.genre}


class Film_Manager:

    def __init__(self):
        self.__repo = []
        with open ('storage_films.json', 'r') as storage_can:
            storage = json.load(storage_can)
            for i in storage:
                self.__repo.append(i)
                 
    def get_all(self):
        m = []
        for i in self.__repo:
            m.append(f"Film {i.get('film')}, Autor {i.get('autor')}, Year {i.get('year')}, Genre {i.get('genre')}")
        return '\n'.join(m)
    
            
    def search(self,serch,by_what):
        rez = []
        for i in self.__repo:
            if (i.get(by_what).find(serch))>-1:
                rez.append(i)
        return rez
    
    def add_new_entry(self, film, autor, year, genre):
        newfilm = Films(film, autor, year, genre)   
        self.__repo.append(newfilm.do_big())
        with open ('storage_films.json', 'w') as storage_can:
            json.dump(self.__repo,storage_can,indent='\t')

