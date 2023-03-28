import oops
from simple_colors import red, green, yellow, blue


def search_for_movie(option_answer: str, searched_str: str):
    """Will return the result where the chosen search option (ex. 'title') consists of the searched string.
    """
    output = oops.RepoActions.search(option_answer, searched_str)
    count = 0
    movies = ''
    for i in output:
        count += 1
        movies += f'{str(count)}. {i}\n'
    if movies:
        print(blue(f"\nHere is the list of movies with {option_answer} like '{searched_str}':\n"))
        print(movies)
    else:
        print("\nThere is no such a movie in your collection")


def no_repo():
    """If there is no list of dict 'repo' it will ask to create a record"""
    print(blue("\nYou don't have any saved movies. Would you like to add one? y/n", 'italic'))
    answer_y = input(yellow("Enter 'y' or 'n': "))
    if answer_y == "y":
        oops.RepoActions.make_repo()
        new_record()
    else:
        main_cycle()


def search_options():
    """Asking to choose one of the search options by number"""
    options = {1: 'title', 2: 'genre', 3: 'year', 4: 'director'}
    for key, value in options.items():
        print(f"{key}. {value.title()}")
    answer_2 = num_option_checker()
    option_answer = options[int(answer_2)]
    print(yellow(f"\nEnter the searched {option_answer} please"))
    return option_answer


def ask_for_search():
    """Will print out anything that was found consider to chosen search option and search string """
    print("\nHow would you like to search? Choose the number")
    option_answer = search_options()
    searched_str = input()
    search_for_movie(option_answer, searched_str)


def num_option_checker():
    """Checking if the input is valid (int, 1-4)"""
    answer_2 = input(yellow("\nEnter the number: "))
    while answer_2.isdigit() and not 0 < int(answer_2) < 5:
        print(red("\nEnter the number between 1 and 4. Let's try again!", 'italic'))
        continue
    return answer_2


def new_record():
    """Will create a new dict and store it to the list 'repo' """
    title = input(yellow("\nEnter a title: "))
    directors_name = input(yellow("Enter a director's name: "))
    year = input(yellow("Enter a year: "))
    genre = input(yellow("Enter a genre: "))
    new_record = oops.Movie(title, directors_name, year, genre)
    my_dict = new_record.my_dct
    oops.RepoActions().write_to_repo(my_dict)
    print(green("\nThe new record was added successfully!"))


def all_movies():
    """Will print all movies from the list 'repo' """
    print(blue("\nHere is the list of movies:", 'italic'))
    # print(oops.RepoActions.read_from_repo())
    for dct in oops.RepoActions.read_from_repo():
        print(f"'{dct['title'].title()}': Directed by {dct['directors_name']}, {dct['year']}, {dct['genre']}")



def main_cycle():
    while True:
        print(blue("\nWould you like to:\n", "italic"))
        print("1.Search for a record\n2.Add a new movie to the collection\n"
              "3.List all movies in the collection\n4.Quit the program ")
        answer = num_option_checker()
        if answer == '1':
            if isinstance(oops.RepoActions.read_from_repo(), str):

                no_repo()
                print("\nWould you still want to search? y/n")
                ask = input(yellow("Enter 'y' or 'n': "))
                if ask == 'y':
                    ask_for_search()
            else:
                ask_for_search()
        elif answer == '2':
            new_record()
            print("\nDo you wanna check your records? y/n")
            answer_y = input(yellow("Enter 'y' or 'n': "))
            if answer_y == "y":
                all_movies()

        elif answer == '3':
            if isinstance(oops.RepoActions.read_from_repo(), str):
                no_repo()
            else:
                all_movies()

        elif answer == '4':
            break

