import logic


def quit():
    print("\nBye!")
    logic.quit()


def get_all_bracelets():

    output = logic.BraceletManage().search('', '')
    print(f"\nAll of your braselets:\n{output}" if output else "Ops")
    anything_else()


def add_new_bracelet():
    material = ask_for_material()
    color = ask_for_color()
    size = ask_for_size()
    sex = ask_for_sex()
    price = ask_for_price()
    logic.BraceletAdd(material, color, size, sex, price).add_new_bracelet()
    print("New bracelet added successfully!")
    anything_else()


def delete_bracelet():
    if logic.BraceletManage().search('', ''):
        print(logic.BraceletManage().search('', ''))
        while True:
            index = input("Select the index of the bracelet you want to delete:\n")
            if logic.BraceletManage().last_index(index):
                logic.BraceletManage().delete_bracelet(index)
                print("Bracelet removed successfully!")
                break
            else:
                print("One does not simply delete something that doesn't exist!")
    else:
        print("Ops")
    anything_else()


def change_price():
    if logic.BraceletManage().search('', ''):
        print(logic.BraceletManage().search('', ''))
        while True:
            index = input("Select the index of the bracelet you want to change price:\n")
            print("Enter the new price:")
            new_price = ask_for_price()
            if logic.BraceletManage().index_proof(index):
                logic.BraceletManage().change_price(index, new_price)
                print("Price changed successfully!")
                break
            else:
                print("One does not simply change something that doesn't exist!")
    else:
        print("Ops")
    anything_else()


def discount(switch):
    while True:
        discount = input("Enter the discount percentage:\n")
        try:
            if 0 < int(discount) < 100:
                discount = int(discount)
                break
            else:
                print("Enter a number from 0 to 100")
        except ValueError:
            print ("Enter a number, please!")
    logic.BraceletManage().discount(switch, discount)
    print("Discount set!")
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

def ask_for_price():
    while True:
        price = input("Уnter the price of the bracelet:\n")
        try:
            if float(price) > 0:
                return float(price)
            else:
                print("Enter a positive number")
        except ValueError:
            print ("Enter a number, please!")

def search_by_material():
    material = ask_for_material()
    output = logic.BraceletManage().search('material', material)
    print_output(output)
    anything_else()


def search_by_color():
    color = ask_for_color()
    output = logic.BraceletManage().search('color', color)
    print_output(output)
    anything_else()


def search_by_size():
    size = ask_for_size()
    output = logic.BraceletManage().search('size', size)
    print_output(output)
    anything_else()


def search_by_sex():
    sex = ask_for_sex()
    output = logic.BraceletManage().search('sex', sex)
    print_output(output)
    anything_else()

def search_by_price():
    while True:
        print("Enter the minimal price")
        min_price = ask_for_price()
        print("Enter the minimal price")
        max_price = ask_for_price()
        if max_price <= min_price:
            print("Try again!")
        else:
            break
    output = logic.BraceletManage().search('price', [min_price, max_price])
    print_output(output)
    anything_else()


def print_output(output):
    print(
        f"\nIt's all with this param:\n{output}" if output else "No bracelets with this param")


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


def change_price_menu():
    while True:
        print("\nChange the price of:")
        print("1. One bracelet\n2. Apply discount to all bracelets\n3. Cancel discount to all bracelets\n0. Return to main menu")
        answer = input()
        if answer == '1':
            change_price()
        elif answer == '2':
            discount(True)
        elif answer == '3':
            discount(False)
        elif answer == '0':
            main_choice()
        else:
            print("Wrong input! Please enter 1-2 or 0!")


def search_main():
    while True:
        print("\nSelect the parameter to search for:")
        print("1. Material\n2. Color\n3. Size\n4. Sex\n5. Price\n0. Return to main menu")
        answer = input()
        if answer == '1':
            search_by_material()
        elif answer == '2':
            search_by_color()
        elif answer == '3':
            search_by_size()
        elif answer == '4':
            search_by_sex()
        elif answer =='5':
            search_by_price()
        elif answer == '0':
            main_choice()
        else:
            print("Wrong input! Please enter 1-5 or 0!")


def main_choice():
    print("\nHi bro! What will we do today?")
    while True:
        print("\n1. Show all bracelets in stock\n2. Add new bracelet\n3. Search any bracelet(s)\n4. Delete any bracelet\n5. Change price\n0. Quit program")
        answer = input()
        if answer == '1':
            get_all_bracelets()
        elif answer == '2':
            add_new_bracelet()
        elif answer == '3':
            search_main()
        elif answer == '4':
            delete_bracelet()
        elif answer =='5':
            change_price_menu()
        elif answer == '0':
            quit()
        else:
            print("Wrong input! Please enter 1-3 or 0!")


if __name__ == "__main__":
    main_choice()
