import back


def print_rez(i):
    print (f"Film: {i.get('film')}, Autor: {i.get('autor')}, Year: {i.get('year')}, Genre: {i.get('genre')}")

def error_input():
    print('\nIncorrect input, try again\n')
    continue_funk() 

def continue_funk():
    print("Return to main menu? y/n")
    dis = input()
    if dis == "y":
        main_men()
    else:
        pass

def all_films():
    for i in back.Films.data_reader():
        print_rez(i)

def add_film():
    print('Enter the title')
    film = input()
    print('Enter the artist')
    artist = input()
    print('Enter the year')
    year = input()
    print('Enter the genre')
    genre = input()
    new = back.Films(film,artist,year,genre)
    back.Films.data_writer(new)

    print(f'\nYou add Title: {film}, Artist: {artist}, Year: {year}, Genre: {genre}')

def serch_by_film():
    print('Input your film')
    y = input()
    for i in back.Films.search(y,'film'):
        print_rez(i)

def serch_by_artist():
    print('Input your artist')
    y = input()
    for i in back.Films.search(y,'autor'):
        print_rez(i)
    
def serch_by_year():
    print('Input your year')
    y = input()
    for i in back.Films.search(y,'year'):
        print_rez(i)

def serch_by(by_what):
    print(f'Enter the {by_what} you are looking for')
    x=0
    y = input()
    for i in back.Films.search(y,f'{by_what}'):
        print_rez(i)
        x=+1
    if x ==0:
        print('Nothing found')

def main_men():
    print('Select a menu item:\n1. Browse all films\n2. Add new\n3. Search\n4. Exit')
    answer = input()
    if answer == '1':
        all_films()
        continue_funk()
    elif answer == '2':
        add_film()
        continue_funk()
    elif answer == '3':
        print('\nSelect a variant of searching:\n1. By title\n2. By artist\n3. By year\n4. By genre')
        answer_2 = input()
        if answer_2 == "1":
            serch_by('film')
            continue_funk()
        elif answer_2 == "2":
            serch_by('autor')
            continue_funk()
        elif answer_2 == "3":
            serch_by('year')
            continue_funk()
        elif answer_2 == "4":
            serch_by('genre')
            continue_funk()
        else:
            error_input()
    elif answer == '4':
        pass
    else:
        error_input()

main_men()
