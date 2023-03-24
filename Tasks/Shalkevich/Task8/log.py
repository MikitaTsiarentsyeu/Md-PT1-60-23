class Films:
    def __init__(self,title,director,year,genre):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
    def alls(self):
         print(self.title + "," + self.director + "," + self.year + "," + self.genre)

def Nev_Film():
    return Films(input("Как называется фильм?"), input("Кто режисёр?"), input("Какого года?"),
                      input("Какого жанра?\n"))
def ALL():
    return film1.alls(),film2.alls(),film3.alls(),film4.alls(),film5.alls(),film6.alls(),film7.alls()


film1 = Films("Christmas trees135", "Whoisthisman!!?", "2036", "Drama")
film2 = Films("Three heroes and the uprising of machines", "Mill", "2037", "Horor")
film3 = Films("The day I sleep", "Never", "2023", "Thriller")
film4 = Films("HOME ALONE REBIRTH", "PLEASEDONOT", "2038", "Horor")
film5 = Films(" ", " "," ", " ")
film6 = Films(" ", " "," ", " ")
film7 = Films(" ", " "," ", " ")

def filtr(Sor):
    f = 0
    if Sor in film1.title and f < 1:
        film1.alls()
        f += 1
    elif Sor in film2.title and f < 1:
        film2.alls()
        f += 1
    elif Sor in film3.title and f < 1:
        film3.alls()
        f += 1
    elif Sor in film4.title and f < 2:
        film4.alls()
    elif Sor in film5.title and f < 1:
        film5.alls()
        f += 1
    elif Sor in film6.title and f < 1:
        film6.alls()
        f += 1
    elif Sor in film7.title and f < 1:
        film7.alls()
        f += 1
    else:
        return Sor, "не найдено"


def filtr_director(Sor):
    f = 0
    if Sor in film1.director and f < 1:
        film1.alls()
        f += 1
    elif Sor in film2.director and f < 1:
        film2.alls()
        f += 1
    elif Sor in film3.director and f < 1:
        film3.alls()
        f += 1
    elif Sor in film4.director and f < 2:
        film4.alls()
    elif Sor in film5.director and f < 1:
        film5.alls()
        f += 1
    elif Sor in film6.director and f < 1:
        film6.alls()
        f += 1
    elif Sor in film7.director and f < 1:
        film7.alls()
        f += 1
    else:
        return Sor, "не найдено"

def filtr_year(Sor):
    f = 0
    if Sor in film1.year and f < 1:
        film1.alls()
        f += 1
    elif Sor in film2.year and f < 1:
        film2.alls()
        f += 1
    elif Sor in film3.year and f < 1:
        film3.alls()
        f += 1
    elif Sor in film4.year and f < 2:
        film4.alls()
    elif Sor in film5.year and f < 1:
        film5.alls()
        f += 1
    elif Sor in film6.year and f < 1:
        film6.alls()
        f += 1
    elif Sor in film7.year and f < 1:
        film7.alls()
        f += 1
    else:
        return Sor, "не найдено"

def filtr_genre(Sor):
    f = 0
    if Sor in film1.genre and f < 1:
        film1.alls()
        f += 1
    elif Sor in film2.genre and f < 1:
        film2.alls()
        f += 1
    elif Sor in film3.genre and f < 1:
        film3.alls()
        f += 1
    elif Sor in film4.genre and f < 2:
        film4.alls()
    elif Sor in film5.genre and f < 1:
        film5.alls()
        f += 1
    elif Sor in film6.genre and f < 1:
        film6.alls()
        f += 1
    elif Sor in film7.genre and f < 1:
        film7.alls()
        f += 1
    else:
        return Sor, "не найдено"
