repo = []


def list_of_movies():
    for dct in repo:
        print(f"{dct['title']}: Directed by {dct['directors_name']}, {dct['year']}, {dct['genre']}")


def add_record(title, directors_name, year, genre):
    dct = {
        'title': title,
        'year': year,
        'directors_name': directors_name,
        'genre': genre
    }
    repo.append(dct)


def search(option, searched_str):
    for dct in repo:
        if searched_str in dct[option]:
            yield f"'{dct['title'].title()}': Directed by {dct['directors_name']}, {dct['year']}, {dct['genre']}"
        else:
            pass



