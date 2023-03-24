import json
biblio = [("Palmer", "Stivens", "2021", "Drama"),
          ("Me time", "Gamburg", "2022", "Comedy"),
          ("Minions", "Kyle Balda", "2022", "Multfilm")]
keys = ["title", "artist/director", "year", "genre"]
    
def writing_to_file():
    res = []
    for biblio_data in biblio:
        biblio_dict = {}
        for i in range(len(keys)):
            biblio_dict[keys[i]] = biblio_data[i]
        res.append(biblio_dict)

        with open("biblio.json", "w") as f:    #склеиваю в файл инф о всех фильмах поочередно
            json.dump(res, f)
    

def add_newRecord(biblio_data):      #добавить новую запись
    biblio.append(biblio_data)
    writing_to_file()     
    return biblio   
   
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
            yield i["year"] #dict(filter(lambda x: "2022" in x.get("year"), data))    
            yield i

def search_genre():
    with open("biblio.json", "r") as f:
        data = json.loads(f.read())
        for i in data:
            yield i["genre"]
            yield i           