class Films:
    def __init__(self,title,director,year,genre):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
    def alls(self):
         print(self.title + "," + self.director + "," + self.year + "," + self.genre)

def Nev_Film(nomber):
    if nomber == 5:
        film5 = Films(input("Как называется фильм?"), input("Кто режисёр?"), input("Какого года?"),
                      input("Какого жанра?\n"))
        return film5
    if nomber == 6:
        film6 = Films(input("Как называется фильм?"), input("Кто режисёр?"), input("Какого года?"),
                      input("Какого жанра?\n"))
        return film6
    if nomber == 7:
        film7 = Films(input("Как называется фильм?"), input("Кто режисёр?"), input("Какого года?"),
                      input("Какого жанра?\n"))
        return film7

film1 = Films("Christmas trees135", "Whoisthisman!!?", "2036", "Drama")
film2 = Films("Three heroes and the uprising of machines", "Mill", "2037", "Horor")
film3 = Films("The day I sleep", "Never", "2023", "Thriller")
film4 = Films("HOME ALONE REBIRTH", "PLEASEDONOT", "2038", "Horor")


Moves =[film1.title,film1.director,film1.year,film1.genre,
        film2.title,film2.director,film2.year,film2.genre,
        film3.title,film3.director,film3.year,film3.genre,
        film4.title,film4.director,film4.year,film4.genre]


def filtr(Sor):
    f = 0
    Sor = Sor
    for i in Moves:
        if i == Sor:
            if i in film1.title and f < 1:
                film1.alls()
                f += 1
            elif i in film2.title and f < 1:
                film2.alls()
                f += 1
            elif i in film3.title and f < 1:
                film3.alls()
                f += 1
            elif i in film4.title and f < 1:
                film4.alls()
                f += 1
            else:
                return Sor, "не найдено"

def filtr_director(Sor):
    f = 0
    Sor = Sor
    for i in Moves:
        if i == Sor:
            if i in film1.director and f < 1:
                film1.alls()
                f += 1
            elif i in film2.director and f < 1:
                film2.alls()
                f += 1
            elif i in film3.director and f < 1:
                film3.alls()
                f += 1
            elif i in film4.director and f < 2:
                film4.alls()
            else:
                return Sor, "не найдено"
def filtr_year(Sor):
    f = 0
    Sor = Sor
    for i in Moves:
        if i == Sor:
            if i in film1.year and f < 1:
                film1.alls()
                f += 1
            elif i in film2.year and f < 1:
                film2.alls()
                f += 1
            elif i in film3.year and f < 1:
                film3.alls()
                f += 1
            elif i in film4.year and f < 2:
                film4.alls()
            else:
                return Sor, "не найдено"
def filtr_genre(Sor):
    f = 0
    Sor = Sor
    for i in Moves:
        if i == Sor:
            if i in film1.genre and f < 1:
                film1.alls()
                f += 1
            elif i in film2.genre and f < 1:
                film2.alls()
                f += 1
            elif i in film3.genre and f < 1:
                film3.alls()
                f += 1
            elif i in film4.genre and f < 2:
                film4.alls()
            else:
                return Sor, "не найдено"


