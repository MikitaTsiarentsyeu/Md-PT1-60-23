import json
import uuid

class Movie:
    def __init__(self, title, artist, year, genre):
        self.__title = title
        self.__artist = artist
        self.__year = year
        self.__genre = genre
        self.__id = uuid.uuid4()

    def get_search_title(self):
        return self.__title
    def get_search_artist(self):
        return self.__artist
    def get_search_year(self):
        return self.__year
    def get_search_genre(self):
        return self.__genre

    def get_id(self):
        return self.__id

    Stitle = property(get_search_title)
    Sartist = property(get_search_artist)
    Syear = property(get_search_year)
    Sgenre = property(get_search_genre)
    id = property(get_id)

objects = []

        #####  Считываем файл репо и создаем обьекты класса согласно репозиторию #####
  
with open ("repo.json", "a", encoding="utf-8") as f:               
    pass

with open ("repo.json", "r", encoding="utf-8") as m:           
    buf = []
    
    try:
        buf = json.load(m)        # Прочитали в буфер
                   
        i = 0
        while i < len(buf):

            x =  Movie(buf[i]["title"],buf[i]["artist"],buf[i]["year"],buf[i]["genre"] )
            objects.append(x)       # Тут храниться список ссылок обьектов
            i += 1
    except:
        pass  

def get_all_movies(): 

    c = []
    for i in objects:
        c.append(i.Stitle)
    return c
    

def Add_a_new_movie(data):

    F = Movie(*data)   # Создали обьект нового класса
    objects.append(F)
    buf = []
    repo = {}

    for g in objects:                   
     
        repo["title"] = g.Stitle
        repo["artist"] = g.Sartist
        repo["year"] = g.Syear
        repo["genre"] = g.Sgenre    
        buf.append(repo)              # Создали список словарей с новым обьектом
        repo = {}

    with open ("repo.json", "w", encoding="utf-8") as f: 
               
        json.dump(buf, f)                     # Записали в файл обновленные данные
        print(buf)  
        print("Запись произведена")     
        
    
def get_movie(answer3, title_s):        # Основная функция поиска (можно искать по:"title", "artist", "year", "genre")
    
    keys = ["title", "artist", "year", "genre"]
    if answer3 == 1: 
        for i in objects:  
            if title_s == i.Stitle: 
                print(f"{i.Stitle}, {i.Sartist}, {i.Syear}, {i.Sgenre}")
    if answer3 == 2: 
        for i in objects:  
            if title_s == i.Sartist: 
                print(f"{i.Stitle}, {i.Sartist}, {i.Syear}, {i.Sgenre}")
    if answer3 == 3: 
        for i in objects:  
            if title_s == i.Syear: 
                print(f"{i.Stitle}, {i.Sartist}, {i.Syear}, {i.Sgenre}")
    if answer3 == 4: 
        for i in objects:  
            if title_s == i.Sgenre: 
                print(f"{i.Stitle}, {i.Sartist}, {i.Syear}, {i.Sgenre}")

def delete_movie(answer5):

    del objects[answer5-1]
    buf = []
    repo = {}

    for g in objects:                   
     
        repo["title"] = g.Stitle
        repo["artist"] = g.Sartist
        repo["year"] = g.Syear
        repo["genre"] = g.Sgenre    
        buf.append(repo)
        repo = {}

    with open ("repo.json", "w", encoding="utf-8") as f: 
               
        json.dump(buf, f)                     # Записали в файл обновленные данные
        print(buf)  
        print("Запись удалена")  

def destroy_database():
    with open("repo.json", "w") as k: 
        pass
