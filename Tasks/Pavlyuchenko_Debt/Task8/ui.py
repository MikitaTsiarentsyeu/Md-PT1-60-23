import logic


def greeting():
    print('''
Hi, DEAR! 
Select an option:
    1 - GET ALL
    2 - ADD A NEW OFFER
    3 - DELETE
    4 - EXIT
''')

def get_all():
    output = logic.ProductManage().search('','')
    print(output)


def enter_data_product():
    print('---ADD NEW PRODUCT---')
    product = input('Enter product: ')
    country = input('Enter country: ')
    variety = input('Enter variety: ')
    caliber = input('Enter caliber: ')
    price = input('Enter price: ')
    logic.PriceAdd(product, country, variety, caliber, price).add_new_product()
    print('---ADDED---')


def delete():
    if logic.ProductManage().search('', ''):
        print(logic.ProductManage().search('', ''))
        while True:
            index = input("Product:\n")
            if logic.ProductManage().last_index(index):
                logic.ProductManage().delete_product(index)
                print("Delete")
                break
            else:
                print("Doesn't exist!")
    else:
        print("Ops")


def main_func():
    greeting()
    while True:
        answer = input('\nSelect: ')
        if answer == '1': get_all()
        elif answer == '2': enter_data_product()
        elif answer == '3': delete()
        elif answer == '0': logic.exit()
        else: print('INCORRECT OPTION')

if __name__ == "__main__":
    main_func()
