import json

with open ("repo.json", "a", encoding="utf-8") as f:               
    pass

def get_all_movies():
        with open ("repo.json", "r", encoding="utf-8") as m:           
            buf = []
            buf = json.load(m)        # Прочитали в буфер
            res = []
            for i in buf:
                res.append(i["title"])
            return res
           
def Add_a_new_album_or_movie(data):
    with open ("repo.json", "r", encoding="utf-8") as m:           
        buf = []
        try:    
            buf = json.load(m)        # Прочитали в буфер 
        except ValueError:
                print("Ошибка чтения. В базе 0 записей.")
    
    repo = {}
    keys = ["title", "artist", "year", "genre"]

    for i in range(4):        
        repo[keys[i]] = data[i]
        
    buf.append(repo)

    with open("repo.json", "w") as k: 
        pass

    with open ("repo.json", "a", encoding="utf-8") as f: 
               
        json.dump(buf, f)                     # Записали в файл обновленные данные
        print(buf)  
        print("Запись произведена")     
                
def get_movie(answer3, title_s):        # Основная функция поиска (можно искать по:"title", "artist", "year", "genre")
    keys = ["title", "artist", "year", "genre"]
    with open ("repo.json", "r", encoding="utf-8") as m:           
        buf = []
        try:    
            buf = json.load(m)        # Прочитали в буфер 
        except ValueError:
                return "Ошибка чтения. Записей в базе нет."
        
    c = (i for i in range(len(buf)))                # Генераторная функция
    search_t = []
    search_t2 = []
    for i in c:
        if buf[i][keys[answer3-1]] == title_s:      # извлекли необходимые индексы по запросу поиска
                search_t.append(i)                 
    for i in search_t:
        search_t2.append(buf[i])                  # положили данные по индексам

    return search_t2

def delete_movie(answer5):
    with open ("repo.json", "r", encoding="utf-8") as m:           
        buf = []
        try:    
            buf = json.load(m)        # Прочитали в буфер 
        except ValueError:
                return "Ошибка чтения. Удалять нечего." 
    del buf[answer5-1]

    with open("repo.json", "w") as k: 
        pass

    with open ("repo.json", "a", encoding="utf-8") as f: 
        
        json.dump(buf, f)                     # Записали в файл обновленные данные
        print(buf)  
        print("Запись удалена")    

def destroy_database():
    with open("repo.json", "w") as k: 
        pass
