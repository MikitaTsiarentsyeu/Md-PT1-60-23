import logic


def quit():
    print("\nBye!")
    logic.quit()


def get_all_bracelets():
    output = logic.get_all_bracelets()
    print(f"\nAll of your braselets:\n{output}" if output else "Ops")
    anything_else()


def add_new_bracelet():
    material = ask_for_material()
    color = ask_for_color()
    size = ask_for_size()
    sex = ask_for_sex()
    logic.add_new_bracelet(material, color, size, sex)
    print("New bracelet added successfully!")
    anything_else()


def ask_for_material():
    return input("Input the material:\n")


def ask_for_color():
    return input("Input the color:\n")


def ask_for_size():
    while True:
        size = input("Input the size:\n")
        if size not in {'xs', 's', 'm', 'l', 'xl'}:
            print("Enter the value according to the size table!")
            continue
        return size


def ask_for_sex():
    while True:
        sex_dict = {'m': 'male', 'f': 'female', 'u': 'unisex'}
        sex = input("Enter m - if male, f - if female, u - if unisex:\n")
        try:
            return sex_dict[sex]
        except KeyError:
            print("There are only 2 genders!!! Try again!")
            continue


def search_by_material():
    material = ask_for_material()
    output = logic.search('material', material)
    print_output(output)
    anything_else()


def search_by_color():
    color = ask_for_color()
    output = logic.search('color', color)
    print_output(output)
    anything_else()

def search_by_size():
    size = ask_for_size()
    output = logic.search('size', size)
    print_output(output)
    anything_else()


def search_by_sex():
    sex = ask_for_sex()
    output = logic.search('sex', sex)
    print_output(output)
    anything_else()


def print_output(output):
    print(f"It's all with this param:\n{output}" if output else "No bracelets with this param")



def anything_else():
    print("\nDo you want to do something else?\nAnswer 'y' if yes, 'n' if no.")
    while True:
        answer = input()
        if answer == 'n':
            quit()
        elif answer == 'y':
            main_choice()
        else:
            print("Input only 'y' or 'n' please.")


def search_main():
    while True:
        print("\nSelect the parameter to search for:")
        print("1. Material\n2. Color\n3. Size\n4. Sex\n0. Return to main menu")
        answer = input()
        if answer == '1':
            search_by_material()
        elif answer == '2':
            search_by_color()
        elif answer == '3':
            search_by_size()
        elif answer == '4':
            search_by_sex()
        elif answer == '0':
            main_choice()
        else:
            print("Wrong input! Please enter 1-4 or 0!")


def main_choice():
    print("\nHi bro! What will we do today?")    
    while True:
        print("\n1. Show all bracelets in stock\n2. Add new bracelet(s)\n3. Search any bracelet(s)\n0. Quit program")
        answer = input()
        if answer == '1':
            get_all_bracelets()
        elif answer == '2':
            add_new_bracelet()
        elif answer == '3':
            search_main()
        elif answer == '0':
            quit()
        else:
            print("Wrong input! Please enter 1-3 or 0!")


if __name__ == "__main__":
    main_choice()
