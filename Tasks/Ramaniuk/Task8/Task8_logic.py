import csv
from csv import writer

class AlbomRepoEntry:
    def __init__(self, title, artist, year, genre):
        self.__title = title
        self.__artist = artist
        self.__year = year
        self.__genre = genre

    def get_title(self):
        return self.__title
    
    def get_artist(self):
        return self.__artist
    
    def get_year(self):
        return self.__year
    
    def get_genre(self):
        return self.__genre
    
    title = property(get_title)
    artist = property(get_artist)
    year = property(get_year)
    genre = property(get_genre)

    def add_title(self, title):
        if title not in self.__title:
            self.__title.append(title)

    def add_artist(self, artist):
        self.__artist.append(artist)

    def add_year(self, year):
        self.__year.append(year)

    def add_genre(self, genre):
        self.__genre.append(genre)
    
class AlbomManager:

    def get_all_records(self):
        with open("Task8.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row['title'],",",row['artist'],",",row['year'],",",row['genre'])
        return "Enjoy"

           
    def get_record_by_title(self, title):
        with open("Task8.csv") as f:
            reader = csv.DictReader(f)
            i = 0
            for row in reader:
                if title == row['title']:
                    print(row['title'],",",row['artist'],",",row['year'],",",row['genre'])
                    i += 1
                else:
                    i += 0
        if i == 0:
            return
        else:
            return "Enjoy"

    def get_record_by_artist(self, artist):
        with open("Task8.csv") as f:
            reader = csv.DictReader(f)
            i = 0
            for row in reader:
                if artist == row['artist']:
                    print(row['title'],",",row['artist'],",",row['year'],",",row['genre'])
                    i += 1
                else:
                    i += 0
        if i == 0:
            return
        else:
            return "Enjoy"

    def get_record_by_year(self, year):
        with open("Task8.csv") as f:
            reader = csv.DictReader(f)
            i = 0
            for row in reader:
                if year == row['year']:
                    print(row['title'],",",row['artist'],",",row['year'],",",row['genre'])
                    i += 1
                else:
                    i += 0
        if i == 0:
            return
        else:
            return "Enjoy"

    def get_record_by_genre(self, genre):
        with open("Task8.csv") as f:
            reader = csv.DictReader(f)
            i = 0
            for row in reader:
                if genre == row['genre']:
                    print(row['title'],",",row['artist'],",",row['year'],",",row['genre'])
                    i += 1
                else:
                    i += 0
        if i == 0:
            return
        else:
            return "Enjoy"

    def add_record(self, title, artist, year, genre):
        new_row = [title, artist, year, genre]    
        with open("Task8.csv",'a', newline = '\n') as f:
            writer_row = writer(f)
            writer_row.writerow(new_row)
            f.close()