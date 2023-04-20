from logica import Logic

class Main:
###################Это для удобства ввода информации от пользователя###########
    def name(self):
        name = input("Please input name\n")
        return name
    def year(self):
        year = input("Please input a year of realised\n")
        return year
    def jenre(self):
        jenre = input("Please input jenre of movie\n")
        return jenre 
    def dir(self):
        dir = input("Please input Director of movie\n")
        return dir
    
####################Функция для добавление фильма в список###################
    def writ(self):
        return Logic.add_func(self.name() ,self.year(), self.jenre(), self.dir())

def main():
    value = input('Hello,how i can help?\nAdd new movie - press 1\nCheck list of movie - press 2\nSearch movie - press 3\n')
    while(True):
        logicForMovie(value)
        value = input('Add new movie - press 1\nCheck list of movie - press 2\nSearch movie - press 3\n')
    
    
def logicForMovie(value):
    main_logic = Main()
    if value == '1': #Добавление
        main_logic.writ()
        print('Movie was added')
    elif value == '2': #Раскрытие всего списка
        print(Logic.q)
    elif value == '3': #Поиск по списку 
        x = input('What criteria will you search for?\n1-Name of movie\n2-Year of the movie\n3-Jenre of movie\n4-Director of movie\n')
        if x == '1':
            print(Logic.gen_name(main_logic.name()))
        elif x == '2':
            print(Logic.gen_year(main_logic.year()))
        elif x == '3':
            print(Logic.gen_jenre(main_logic.jenre()))
        elif x == '4':
            print(Logic.gen_dir(main_logic.dir()))


if __name__ == '__main__':
    main()