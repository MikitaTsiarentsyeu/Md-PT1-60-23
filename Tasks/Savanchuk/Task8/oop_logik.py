import json
class MovieBiblio:

    def __init__(self, title, artist, year, genre):
        self.__title = title
        self.__artist = artist
        self.__year = year
        self.__genre = genre
        
    def get_title(self):
        return self.__title
    def set_title(self, title):
        self.__title = title

    def get_artist(self):
        return self.__artist
    def set_artist(self, artist):
        self.__artist = artist   

    def get_year(self):
        return self.__year
    def set_year(self, year):
        self.__year = year    

    def get_genre(self):
        return self.__genre
    def set_genre(self, genre):
        self.__genre = genre    

    title = property(get_title, set_title)
    artist = property(get_artist, set_artist)
    year = property(get_year, set_year)
    genre = property(get_genre, set_genre)

    def writing_to_file(self):
        with open("biblio.json", "r") as f:
            data = json.loads(f.read())
            data.append({'title':self.title, 'artist':self.artist, 'year':self.year, 'genre':self.genre})
        with open("biblio.json", "w") as f:
            json.dump(data, f)
        
    def list_allAlbums():
        with open("biblio.json", "r") as f:
            read = f.read()
        return read    
    
    def search_title():
        with open("biblio.json", "r") as f:
            data = json.loads(f.read())
            for i in data:
                yield i["title"]   
                yield i

    def search_artist():
        with open("biblio.json", "r") as f:
            data = json.loads(f.read())
            for i in data:
                yield i["artist/director"]
                yield i

    def search_year():
        with open("biblio.json", "r") as f:
            data = json.loads(f.read())
            for i in data:
                yield i["year"]     
                yield i

    def search_genre():
        with open("biblio.json", "r") as f:
            data = json.loads(f.read())
            for i in data:
                yield i["genre"]
                yield i           