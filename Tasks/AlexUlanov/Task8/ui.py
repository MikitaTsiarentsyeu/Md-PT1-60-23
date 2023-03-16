import logic
from art import tprint

def main_cycle ():
    while True:
        tprint("Hello")
        print("Select item from the menu:")
        print("1.Add a new movie to the collection")
        print("2.List all movies in the collection")
        print("3.Search for movie by title, artist, year, or genre.")
        print("4.Quit the program.")
        print("5.Delete movie from base")
        print("6.Search and destroy all database")
        answer = input()
        if answer == "1":
            while True:
                title = input("please enter movie title. If you make a misstake just tab '5'\n")
                artist = input("please enter movie artist\n")
                year = input("please enter movie year\n")
                genre = input("please enter movie genre\n")
                logic.Add_a_new_album_or_movie([title, artist, year, genre])
                print("ok")
                break

        if answer == "2":
            output = logic.get_all_movies()
            print(f"\nMovies in collection:\n")
            for i in range(len(output)):
                print(f"{i+1}.{output[i]}")
            
        if answer == "3":
            while True:
                print("\nChose search for movie by:\n 1.title\n 2.artist\n 3.year\n 4.genre")
                answer3 = int(input())


                if 5 > answer3 > 0:
                    keys = ["title", "artist", "year", "genre"]

                    title_s = input(f"Enter {keys[answer3-1]}\n")
                    res3 = logic.get_movie(answer3, title_s)
                    print(f"{keys[answer3-1]} by your term:")
                    for i in range(len(res3)):
                        print(f"{i+1}.{res3[i]}")
                break
                
        if answer == "4":
            break

        if answer == "5":
            output = logic.get_all_movies()
            print(f"\nMovies in collection:\n")
            for i in range(len(output)):
                print(f"{i+1}.{output[i]}")
            answer5 = int(input("Which movie do you want to delete?\nSelect the number from list.\n"))
            logic.delete_movie(answer5)

        if answer == "6":
            logic.destroy_database()
            tprint("nice")

main_cycle()


