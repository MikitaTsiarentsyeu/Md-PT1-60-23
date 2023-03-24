import logic

def get_all_films():
    output = logic.get_all_films()
    print_output(output)

def add_film():
    name = ask_for_name()
    year = ask_for_year()
    producer = ask_for_producer()
    genre = ask_for_genre()
    logic.add_film(name, producer, year, genre)
    

def ask_for_year():
    return input("Input the year:\n")
def ask_for_producer():
    return input("Input the producer:\n")    

def ask_for_name():
    return input("Input the name:\n")

def ask_for_genre():
    return input("Input the genre:\n")

def print_output(output):
    print(output if output else "no records")

def main_cycle():
    while True:
        print("\nSelect an item from the menu:")
        print("1.Browse all films\n2.Get record\n3.Add record")
        answer = input()
        if answer == '1':
            get_all_films()
        elif answer == '2':
            logic.get_record_by_name(ask_for_name())
        elif answer == '3':
            add_film()
        else:
            break    

if __name__ == "__main__":
    main_cycle()        