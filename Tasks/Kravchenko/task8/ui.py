import logic

def add_new_record():
    title = input('Enter the album title\n')
    artist = input('Enter the artist name\n')
    year = input('Enter the album production year\n')
    genre = input('Enter the genre\n')
    logic.add_record(title, artist, year, genre)
    print(logic.repo)

def search_the_album_by_option():
    print("\n Choose the option how would you like to search the musical album:")
    print("1. By title\n2. By artist\n3. By year\n4. By genre")
    option = input('Enter a number\n')
    search_options(option)


def search_options(option):
    options = {'1': 'title', '2': 'artist', '3': 'year', '4': 'genre'}
    user_response = input(f"Enter {options[option]}\n")
    logic.search_by_option(options[option], user_response)
    for i in logic.search_by_option(options[option], user_response):
        print(i)


def main_cycle():
    while True:
        print("\nSelect an item from the menu:")
        print("1.Add a new album to the collection\n2.Get all albums in the collection\n"
              "3.Search for the album\n4. Quit the program")
        answer = input()
        if answer == '1':
            add_new_record()
        elif answer == '2':
            logic.get_all_albums()  
        elif answer == '3':
            search_the_album_by_option()    
        else:
            break


if __name__ == "__main__":
    main_cycle()

