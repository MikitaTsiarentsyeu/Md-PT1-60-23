import log

def cycle():
    count = 0
    film5 = log.Films(" ", " ", " ", " ")
    film6 = log.Films(" ", " ", " ", " ")
    film7 = log.Films(" ", " ", " ", " ")

    while True:
        print("\nВыберите пункт из меню:"
              "\n1. Добавить новую запись\n2. Вывести список всех альбомов\n3. Найти альбом или фильм\n4.Выйти.")
        answer = input()
        if answer == "1":
            print("вы можете доабавить дополнительно не более чем три файла")
            answer = input("хотите добавить файл?")
            if answer == "Да":
                    if count < 1:
                        film5 = log.Nev_Film(5)
                        count =+ 1
                        continue
                    elif count == 1:
                        film6 = log.Nev_Film(6)
                        count =+ 1
                        continue
                    else:
                        film7 = log.Nev_Film(7)
                        continue
            else:
                continue
        elif answer == "2":
            log.Films.alls(log.film1), log.Films.alls(log.film2),log.Films.alls(log.film3),log.Films.alls(log.film4),
            log.Films.alls(film5), log.Films.alls(film6),log.Films.alls(film7)
        elif answer == "3":
            print("\nВыберите элемент для поиска:\n"
                  "1.Поиск по названию\n2.Поиск по исполнителю/режиссёру\n3.Поиск по году\n4.Поиск по жанру")
            answer2 = input()
            if answer2 == "1":
                answer = input("что ищим?")
                log.filtr(answer)
                if answer in film5.title:
                    film5.alls()
                elif answer in film6.title:
                    film6.alls()
                elif answer in film7.title:
                    film7.alls()
            elif answer2 == "2":
                answer = input("что ищим?")
                log.filtr_director(answer)
                if answer in film5.director:
                    film5.alls()
                elif answer in film6.director:
                    film6.alls()
                elif answer in film7.director:
                    film7.alls()
            elif answer2 == "3":
                answer = input("что ищим?")
                log.filtr_year(answer)
                if answer in film5.year:
                    film5.alls()
                elif answer in film6.year:
                    film6.alls()
                elif answer in film7.year:
                    film7.alls()
            elif answer2 == "4":
                answer = input("что ищим?")
                log.filtr_genre(answer)
                if answer in film5.genre:
                    film5.alls()
                elif answer in film6.genre:
                    film6.alls()
                elif answer in film7.genre:
                    film7.alls()
                try:
                    True
                except AttributeError:
                    continue
            else:
                break
        elif answer == "4":
            break

cycle()