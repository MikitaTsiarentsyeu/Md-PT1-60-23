repo = [{'title': 'Creep EP', 'artist': 'Radiohead',  'year': '1992', 'genre': 'indie'},
        {'title': 'The Resistance','artist': 'Muse',  'year': '2009', 'genre': 'alternative'},
        {'title': 'Back To Black', 'artist': 'Amy Winehouse', 'year': '2007', 'genre': 'soul'}]

def add_record(title, artist, year, genre):
    record = {'title': title, 'artist': artist, 'year': year, 'genre': genre}
    repo.append(record)

def get_all_albums():
    for record in repo:
        print(f" '{record['title']}' by {record['artist']} ({record['year']}, {record['genre']})")



def search_by_option(option, user_response):
   for record in repo:
        if user_response in record[option]:
            yield f" '{record['title']}' by {record['artist']} ({record['year']}, {record['genre']})"
       
