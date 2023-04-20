import csv
from model import Album


class AlbumService:
    FILENAME = "albums.csv"

    def __init__(self):
        self.albums = []
        self.load_data()

    def add_record(self, title: str, artist: str, year: int, genre: str):
        self.albums.append(Album(title, artist, year, genre))
        # append single record into new line in the file
        with open(self.FILENAME, "a") as file:
            file.write(f"{title},{artist},{year},{genre}\n")

    def get_all_albums(self):
        for album in self.albums:
            print(album)

    def load_data(self):
        # load data from file and skip the header
        with open(self.FILENAME, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                self.albums.append(Album(row[0], row[1], row[2], row[3]))

    def search_by_option(self, option: str, search_term: str):
        if option == "title":
            return self.search_title(search_term)
        elif option == "artist":
            return self.search_artist(search_term)
        elif option == "year":
            return self.search_year(search_term)
        elif option == "genre":
            return self.search_genre(search_term)

    def search_title(self, search_term: str):
        for album in self.albums:
            if search_term in album.title:
                yield album

    def search_artist(self, search_term: str):
        for album in self.albums:
            if search_term in album.artist:
                yield album

    def search_year(self, search_term: str):
        for album in self.albums:
            if search_term in album.year:
                yield album

    def search_genre(self, search_term: str):
        for album in self.albums:
            if search_term in album.genre:
                yield album
