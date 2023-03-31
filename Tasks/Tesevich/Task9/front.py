import back

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
    x = back.Film_Manager()
    print(x.get_all())
    

def add_film():
    print('Enter the title')
    film = input()
    print('Enter the artist')
    artist = input()
    print('Enter the year')
    year = input()
    print('Enter the genre')
    genre = input()
    new = back.Film_Manager() 
    new.add_new_entry(film, artist, year, genre)
    print(f'\nYou add Title: {film}, Artist: {artist}, Year: {year}, Genre: {genre}')


def serch_by(by_what):
    print(f'Enter the {by_what} you are looking for')
    x=0
    y = input()
    serch = back.Film_Manager()
    rez = serch.search(y,f'{by_what}')
    if len(rez) <1:
        print('Nothing found')
    else:
        print("Your result:")
        for i in rez:
            print (f"Film: {i.get('film')}, Autor: {i.get('autor')}, Year: {i.get('year')}, Genre: {i.get('genre')}")


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
