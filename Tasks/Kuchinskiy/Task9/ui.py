import oop_logic

def get_all_movies():
    list_of_list = oop_logic.Movie.get_all_movies()
    for item in list_of_list:
        print(' '.join(item))

def add_new_movie(): 
    name = input('Enter movie name:\n')
    director = input('Enter the name of the film director:\n')
    year = str(input('Enter the year of the movie:\n'))
    genre = input('Enter movie genre:\n')
    oop_logic.add_new_film(name, director, year, genre)

def search_movie():
    keys = input()
    if keys == "title":
        inp = input('Enter movie name:\n')
    elif keys == "director":
        inp = input('Enter the name of the film director:\n')
    elif keys == "year":
        inp = input('Enter the year of the movie:\n')
    elif keys == "genre":
        inp = input('Enter movie genre:\n')
    output = oop_logic.Movie.search_movie(inp, keys)
    print(output if output else "no movies")

def main_cycle():
    while True:
        print("\nSelect an item from the list:\n")
        print("1 - Show all movies\n"
        "2 - Add a new movie\n"
        "3 - Search movie\n"
        "4 - Exit\n")
        answer = input()
        if answer == '1':
            get_all_movies()
        elif answer == '2':
            add_new_movie()
        elif answer == '3':
            print("select search criteria:")
            print("title")
            print("director")
            print("year")
            print("genre")
            search_movie()
        elif answer == '4':
            exit()
        else:
            print("choose right number")

if __name__ == "__main__":
    main_cycle()