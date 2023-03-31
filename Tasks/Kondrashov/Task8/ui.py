import logic
import sep
import os



def add_film():
    res = logic.save_film()
    if res:
        print("\033[36mYour film was added")
    else:
        print("Something went wrong")


def search():
    content = input('Please provide one parameter: \nTitle | Director | Year of release | Genre\n').strip().capitalize()
    print(content)
    res = logic.search_film(content)
    if res:
        for i in range(len(res)):
            print('Title:', res[i][0])
            print('Director:', res[i][1])
            print('Year of release:', res[i][2])
            print('Genre:', res[i][3])
    else:
        print('Oops... Something went wrong:(')


def validate_separator(ask):
    while True:
        name = input(ask).strip().title()
        if const.SEP in name:
            print(f"Please don't use {const.SEP} in your text")
            continue
        if name == '':
            print('Please write something')
            continue
        break
    return name


def show_menu():
    while True:
        print("\033[0m1. Add new film")
        print("2. Search film")
        print("3. View all films")
        print("4. Exit")
        answer = input("Choose any position from the list above:\n")
        if answer == "1":
            add_film()
        elif answer == "2":
            search()
        elif answer == "3":
            c = open(logic.file)
            line = c.readlines()
            print(*line)
        elif answer == "4":
            print('Have a nice day!')
            break
        else:
            print("Please, you need to choose action number from this list...")
            continue

show_menu()