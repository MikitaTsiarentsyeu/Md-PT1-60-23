import Task8_logic

logic = Task8_logic.AlbomManager()

def get_all_records():
    output = logic.get_all_records()
    print_output(output)

def get_record_by_title():
    title = ask_for_title()
    output = logic.get_record_by_title(title)
    print_output(output)

def get_record_by_artist():
    artist = ask_for_artist()
    output = logic.get_record_by_artist(artist)
    print_output(output)

def get_record_by_year():
    year = ask_for_year()
    output = logic.get_record_by_year(year)
    print_output(output)

def get_record_by_genre():
    genre = ask_for_genre()
    output = logic.get_record_by_genre(genre)
    print_output(output)

def add_record():
    title = ask_for_title()
    artist = ask_for_artist()
    year = ask_for_year()
    genre = ask_for_genre()
    logic.add_record(title, artist, year, genre)
    get_all_records()

def ask_for_title():
    return input("Input the title:\n")

def ask_for_artist():
    return input("Input artist:\n")

def ask_for_year():
    return input("Input year:\n")

def ask_for_genre():
    return input("Input the genre:\n")

def print_output(output):
    print(output if output else "no records")

def main_cycle():
    while True:
        print("\nSelect an item from the menu:")
        print("1.Browse all records\n2.Get record\n3.Add record")
        answer = input()
        if answer == '1':
            get_all_records()
        elif answer == '2':
            print("1.Get record by title\n2.Get record by artist\n3.Get record by year\n4.Get record by genre")
            answer_2 = input()
            if answer_2 == '1':
                get_record_by_title()
            elif answer_2 == '2':
                get_record_by_artist()
            elif answer_2 == '3':
                get_record_by_year()
            elif answer_2 == '4':
                get_record_by_genre()
            else:
                break
        elif answer == '3':
            add_record()
        else:
            break


if __name__ == "__main__":
    main_cycle()