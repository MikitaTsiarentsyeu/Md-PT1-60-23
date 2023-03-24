import csv
from prettytable import from_csv


def add_record(title, name, year, genre):
    with open('base.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([f'{title}', f'{name}', f'{year}', f'{genre}'])


def get_all_movies():
    with open("base.csv", 'r', newline='', encoding='utf-8') as fp:
        mytable = from_csv(fp)
        mytable.align = "l"
        print(mytable if mytable else "no movies")


def search(search_str):
    with open("base.csv", 'r', newline='', encoding='utf-8') as file:
        read = csv.reader(file, delimiter=',')
        for i in read:
            if search_str in i:
                yield f"{i[0]}, {i[2]}, {i[3]} - Directed by {i[1]}"
            else:
                pass


def search_for_movie(item_answer, search_str):
    output = search(search_str)
    count = 0
    films = ''
    for i in output:
        count += 1
        films += f'{str(count)}. {i}\n'
    if films:
        print(f"\nFound by your request '{search_str}':\n")
        print(films)
    else:
        print("\nWe don't have this movie.")


def search_options():
    menu_items = {1: 'Title', 2: 'Director', 3: 'Year', 4: 'Genre'}
    for key, value in menu_items.items():
        print(f"{key}. {value.title()}")
    menu_item = input("\nEnter the item: ")

    if menu_item.isdigit() and 1 <= int(menu_item) <= 4:
        item_answer = menu_items[int(menu_item)]
        print(f"\nEnter the searched {item_answer} please")
        return item_answer
    else:
        print("\nEnter the item between 1 and 4. Let's try again! (press Enter)")
