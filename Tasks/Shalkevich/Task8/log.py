import json
list = [("Christmas trees135", "Whoisthisman!!?", "2036", "Drama"),
          ("Three heroes and the uprising of machines", "Mill", "2037", "Horor"),
          ("The day I sleep", "Never", "2023", "Thriller"),
          ("HOME ALONE REBIRTH", "PLEASEDONOT", "2038", "Drama")]
typs = ["title", "artist/director", "year", "genre"]

def writ():
    res = []
    for films in list:
        film = {}
        for i in range(len(typs)):
            film[typs[i]] = films[i]
        res.append(film)

        with open("film.json", "w") as f:
            json.dump(res, f)

def add_newRecord(biblio_data):
    list.append(biblio_data)
    writ()
    return list

def list_all():
    with open("film.json", "r") as f:
        read = f.read()
    return read


def title():
    with open("film.json", "r") as f:
        data = json.loads(f.read())
        for i in data:
            yield i["title"]
            yield i

def derect():
    with open("film.json", "r") as f:
        data = json.loads(f.read())
        for i in data:
            yield i["artist/director"]
            yield i

def year():
    with open("film.json", "r") as f:
        data = json.loads(f.read())
        for i in data:
            yield i["year"]
            yield i

def genre():
    with open("film.json", "r") as f:
        data = json.loads(f.read())
        for i in data:
            yield i["genre"]
            yield i