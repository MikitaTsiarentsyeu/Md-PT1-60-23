repo = [
      { "name": "The Disgusting Eight", "producer": "Quentin Tarantino", "year": 2015, "genre": "Drama"},
    { "name": "Interrupted life", "producer": "James Mangold", "year": 1999, "genre": "Drama"},
    { "name": "Misfits", "producer": "Howard Overman", "year": 2009, "genre": "fantasy"},
]



def add_film(name, producer, year, genre):
    isFound = false
    for i in repo:
        if i[name] == name:
           i[year] = year
           i[producer] = producer
           i[genre] = genre
           isFound = true

    if isFound == false:
        repo.append({ "name": name, "producer": producer, "year": year, "genre": genre})


def get_all_films():
    return '\n'.join([f"{i["name"]}:{','.join(i["producer"], i["year"], i["genre"])}" for i in repo])
    
    

def get_record_by_name(name):
    try:
        numbers = repo[name]
        return f"{name}:{','.join(numbers)}" 
    except KeyError:
        return ""