import log

def add_new():
    biblio_data = input("Введите название, исполнителя/режиссера, год, жанр через пробел")
    biblio_data = list(biblio_data.title().split())
    log.add_newRecord(biblio_data)

def list_all():
    read = log.list_all()
    print(read)

def by(gener):
    try:
        name = input("Введите искомое слово:")
        name = name.title()
        while True:
            for i in gener:
                if name in i:
                    print(f"{next(gener)}\n")
            else:
                next(gener)
    except StopIteration:
        print("Ничего нет!")

def cycle():
    while True:
        print("\nВыберите пункт из меню:"
              "\n1. Добавить новую запись\n2. Вывести список всех альбомов\n3. Найти альбом или фильм\n4.Выйти.")
        answer = input()
        if answer == "1":
            add_new()
        elif answer == "2":
            list_all()
        elif answer == "3":
            print("\nВыберите элемент для поиска:\n"
                  "1.Поиск по названию\n2.Поиск по исполнителю/режиссёру\n3.Поиск по году\n4.Поиск по жанру")
            answer2 = input()
            if answer2 == "1":
                by(log.title())
            elif answer2 == "2":
                by(log.derect())
            elif answer2 == "3":
                by(log.year())
            elif answer2 == "4":
                by(log.genre())
            else:
                break
        elif answer == "4":
            break

cycle()