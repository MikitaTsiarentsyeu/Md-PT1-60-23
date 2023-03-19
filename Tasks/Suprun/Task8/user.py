import logic
def add_a_new_movie():
    title = ask_for_title()
    director = ask_for_director()
    year = ask_for_year()
    genre = ask_for_genre()
    logic.add_a_new_movie(title, director, year, genre)
    get_all_movies()

def get_all_movies():
    for i in logic.get_all_movies():
        print(i)

def search(item):
    for i in logic.search(item):
        print(i)
       
def ask_for_title():
    return input("Input the title:\n")

def ask_for_director():
    return input("Input the director:\n")

def ask_for_year():
    while True:
        num = input("Input the year(4-digit number):\n")
        for i in num:
            if len(i) != 4 or not i.isdigit():
                continue
        return num
       
def ask_for_genre():
    return input("Input the genre:\n")

def main_cicle():
    while True:
        print("\nSelect an item from the menu:")
        print("1.Add a new movie\n2.Get all movies\n3.Search movie\n4.Quit the program")
        answer = input()
        if answer == '1':
            add_a_new_movie()
        elif answer == '2':
            get_all_movies()
        elif answer == '3':
            print("\nSelect an item from the menu:")
            print("1.Search by title\n2.Search by director\n3.Search by year\n4.Search by genre")
            second_answer = input()
            if second_answer == '1':
                title = ask_for_title()
                search(title)
            elif second_answer == '2':
                director = ask_for_director()
                search(director)
            elif second_answer == '3':
                year = ask_for_year()
                search(year)
            elif second_answer == '4':
                genre = ask_for_genre()
                search(genre)
        elif answer == '4':
            break
