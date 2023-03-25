import logic
import re


def view_menu():
    output = logic.view_menu()
    print(output)


def search_sushi():
    search = ask_search()
    output = logic.search_sushi(search)
    print(output)


def add_info():
    name = ask_name()
    email = ask_email()
    logic.add_info(name, email)
    print(f"{name} is registered! Thank you! ")
    # get_all_records()


def ask_search():
    search = input("Search food, for example 'Суши':\n")
    return search


def ask_name():
    name = input("Enter your name:\n")
    return name


def ask_email():
    max_inp = 3
    num_inp = 0
    while num_inp < max_inp:
        try:
            email_inp = input("Enter your email:\n")
        except KeyboardInterrupt:
            print("\nExiting Program...")

        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(pattern, email_inp):
            return email_inp
        else:
            print("\nInvalid email address!\nTry again!\n")
            num_inp += 1
    print("Max attempts reached. Exiting program...")

    exit()


def main():
    while True:
        print("\nChoose what you want to do:")
        print(
            "\n Press 1 for show menu\n Press 2 for search food from menu\n Press 3 for registration\n Press 4 for exite\n")
        try:
            choise = input()
            if choise == '1':
                view_menu()
            elif choise == '2':
                search_sushi()
            elif choise == '3':
                add_info()
            elif choise == '4':
                break
            else:
                print("Invalid choice. Please enter a valid option (1-4).")
        except ValueError:
            print("Invalid input. Please enter a number (1-4):\n")


if __name__ == '__main__':
    main()
