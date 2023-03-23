import log

def cycle():
    count = 0
    while True:
        print("\nВыберите пункт из меню:"
              "\n1. Добавить новую запись\n2. Вывести список всех альбомов\n3. Найти альбом или фильм\n4.Выйти.")
        answer = input()
        if answer == "1":
            print("вы можете доабавить дополнительнj 3 файла")
            if count == 0:
                log.film5 = log.Nev_Film()
                count +=1
            elif count == 1:
                log.film6 = log.Nev_Film()
                count += 1
            elif count == 2:
                log.film7 = log.Nev_Film()
            else:
                log.film10 = log.Nev_Film()
        elif answer == "2":
            log.ALL()
        elif answer == "3":
            print("\nВыберите элемент для поиска:\n"
                  "1.Поиск по названию\n2.Поиск по исполнителю/режиссёру\n3.Поиск по году\n4.Поиск по жанру")
            if answer2 == 1:
                log.filtr(input("что искать?"))
            elif answer2 == 2:
                log.filtr_director(input("что искать?"))
            elif answer2 == 3:
                log.filtr_year(input("что искать?"))
            elif answer2 == 4:
                log.filtr_genre(input("что искать?"))
            else:
                continue
        elif answer == "4":
            break

cycle()