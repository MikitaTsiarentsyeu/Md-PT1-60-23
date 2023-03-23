import csv

FILENAME = "C:/Users/Acer/Documents/GitHub/Md-PT1-60-23/Tasks/Sergeichik_Maria/Task8/films.csv"

repo = [
    { "name": "The Disgusting Eight", "producer": "Quentin Tarantino", "year": 2015, "genre": "Drama"},
    { "name": "Interrupted life", "producer": "James Mangold", "year": 1999, "genre": "Drama"},
    { "name": "Misfits", "producer": "Howard Overman", "year": 2009, "genre": "fantasy"},
]
nameKey = "name"
producerKey = "producer"
yearKey = "year"
genreKey = "genre"


def add_film(name, producer, year, genre):

    isFound = False
    newFilm = dict()
    with open(FILENAME, "r") as file:
        localRepo = csv.DictReader(file)

        for i in localRepo:
            if str(i[nameKey]) == str(name):
                i[yearKey] = year
                i[producerKey] = producer
                i[genreKey] = genre
                isFound = True

        if isFound == False:
            newFilm = dict({ nameKey: name, producerKey: producer, yearKey: year, genreKey: genre})

    if isFound == False:
        with open(FILENAME, 'a', newline='') as file:
            print(newFilm[nameKey])
            #writer = csv.writer(file)
            writer = csv.DictWriter(file)
            writer.writerow(newFilm)
            #columns = [nameKey, producerKey, yearKey, genreKey]
            #writer = csv.DictWriter(file, fieldnames=columns)
            #writer.writeheader()
            


def get_all_films():

    str = ""
    localRepo = dict()
    with open(FILENAME, "r", newline="") as file:
        localRepo = csv.DictReader(file)

    for i in localRepo:
        str += "\n"
        str += f"{i[nameKey]}"
        str += f"{i[producerKey], i[yearKey], i[genreKey]}"

    return str
    
    

def get_record_by_name(name):
    try:
        numbers = repo[name]
        return f"{name}:{','.join(numbers)}" 
    except KeyError:
        return ""