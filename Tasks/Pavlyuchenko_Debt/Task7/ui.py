import logic


def greeting():
    print('''
Hi, DEAR! 
Select an option:
    1 - SHOW PRICE LIST
    2 - ADD A NEW OFFER
    3 - SELECT BY PARAMETR
    4 - EXIT
''')

def get_all():
    print('---PRICE LIST---')
    price = logic.get_all()
    print(price)


def enter_data_product():
    print('---ADD NEW PRODUCT---')
    logic.add_new_product([(input(f'Enter {i}: ')).lower() for i in logic.keys_data])
    print('---ADDED---')


def enter_search():
    try:
        print('---SEARCH: ENTER KEY AND VALUE---\n')
        key = (input('Key(week, product, country): ')).lower()
        value = input('Value: ').lower()
        print('\n---SEARCH RESULT---')
        search = logic.search_key_value(key, value)
        print(search)
    except KeyError:
        print('NOT FOUND KEY/VALUE')

def enter_search_key():
    try:
        print('---SEARCH: ENTER KEY AND VALUE---\n')
        key = (input('Key(week, product, country): ')).lower()
        print('\n---SEARCH RESULT---')
        search = logic.search_key(key)
        print(search)
    except KeyError:
        print('NOT FOUND KEY/VALUE')


def main_func():
    greeting()
    while True:
        answer = input('\nSelect: ')
        if answer == '1': get_all()
        elif answer == '2': enter_data_product()
        elif answer == '3': enter_search()
        elif answer == '4': enter_search_key
        elif answer == '0': logic.exit()
        else: print('INCORRECT OPTION')

if __name__ == "__main__":
    main_func()
