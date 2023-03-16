import back


def add_record():
    title = input("Input the title:\n")
    name = input("Input the director name:\n")
    year = input("Input the year:\n")
    genre = input("Input the genre:\n")
    back.add_record(title, name, year, genre)


def get_all_records():
    print('The following entries were found for your request:')
    back.get_all_movies()


def find_movie():
    print("\nHow would you like to search? Choose the number")
    item_answer = back.search_options()
    search_str = input()
    back.search_for_movie(item_answer, search_str)


def main_page():
    while True:
        print("\nSelect an item from the menu:")
        print("1.Browse all films\n2.Find film\n3.Add new film")
        answer = input()
        if answer == '1':
            get_all_records()
        elif answer == '2':
            find_movie()
        elif answer == '3':
            add_record()
        else:
            print('Incorrect input')
            #break
