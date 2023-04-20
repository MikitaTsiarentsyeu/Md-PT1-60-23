from backend import AlbumService


def search_the_album_by_option():
    print("\n Choose the option how would you like to search the musical album:")
    print("1. By title\n2. By artist\n3. By year\n4. By genre")
    option = input('Enter a number\n')
    search_options(option)


def search_options(option):
    service = AlbumService()
    options = {'1': 'title', '2': 'artist', '3': 'year', '4': 'genre'}
    user_response = input(f"Enter {options[option]}\n")
    for i in service.search_by_option(options[option], user_response):
        print(i)


if __name__ == '__main__':
    service = AlbumService()

    while True:
        print("\nSelect an item from the menu:")
        print("1.Add a new album to the collection\n2.Get all albums in the collection\n"
              "3.Search for the album\n4.Quit the program")
        answer = input()
        if answer == '1':
            title = input('Enter the album title\n')
            artist = input('Enter the artist name\n')
            year = int(input('Enter the album production year\n'))
            genre = input('Enter the genre\n')
            # Add a new record
            service.add_record(title, artist, year, genre)
        elif answer == '2':
            # Get all albums
            service.get_all_albums()
        elif answer == '3':
            search_the_album_by_option()
        else:
            break
