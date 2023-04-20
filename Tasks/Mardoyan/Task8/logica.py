import json

from dto import FilmDTO

class Logic:

    q = None

    with open('films.json','r') as file1:
        q = json.load(file1)
######Функция добавления######

    def add_func(name,year,jenre,dir):
        d = {
            'name' : name ,
            'year' : year ,
            'jenre' : jenre,
            'dir' : dir
        }
        film = FilmDTO(name=name, year=year, jenre=jenre, dir=dir)

        Logic.q.append(film.dict())
        
        with open('films.json','w',encoding='utf-8') as file1:
            data = json.dump(Logic.q,file1)
##########Генераторы поиска#######        
    @staticmethod
    def gen_name(name):
        for i in Logic.q:
            if name == i['name']:
                return i
    @staticmethod
    def gen_year(year):
        spis = []
        for i in Logic.q:
            if year == i['year']:
                spis.append(i)
        if len(spis) > 0:
            return spis
        else:
            return 'Movie was not founded'

    @staticmethod
    def gen_jenre(jenre):
        spis = []
        for i in Logic.q:
            if jenre == i['jenre']:
                spis.append(i)
        if len(spis) > 0:
            return spis
        else:
            return 'Movie was not founded'
    
    @staticmethod
    def gen_dir(dir):
        spis = []
        for i in Logic.q:
            if dir == i['dir']:
                spis.append(i)
        if len(spis) > 0:
            return spis
        else:
            return 'Movie was not founded'
    
    
        









