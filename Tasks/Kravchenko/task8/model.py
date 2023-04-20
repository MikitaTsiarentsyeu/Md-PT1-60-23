

class Album:
    def __init__(self, title, artist, year, genre):
        self.__title = title
        self.__artist = artist
        self.__year = year
        self.__genre = genre

    def __str__(self):
        return f"{self.__title}, {self.__artist}, {self.__year}, {self.__genre}"

    def __repr__(self):
        return f"{self.__title}, {self.__artist}, {self.__year}, {self.__genre}"

    @property
    def title(self):
        return self.__title

    @property
    def artist(self):
        return self.__artist

    @property
    def year(self):
        return self.__year

    @property
    def genre(self):
        return self.__genre

    @property
    def entry(self) -> dict:
        return {
            "title": self.__title,
            "artist": self.__artist,
            "year": self.__year,
            "genre": self.__genre
        }





