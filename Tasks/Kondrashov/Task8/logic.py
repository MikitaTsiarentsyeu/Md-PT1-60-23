import os
import sep


name = 'films.txt'
directory = 'repo'
file = os.path.join(directory, name)


class Films:
    def __init__(self, title, director, year, genre):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre


def save_film():
    content = Films(input("Please, input a film title:\n"), input("Input the film director:\n"),
    input("Input film release year:\n"), input("Input film genre:\n"))
    content = f'{content.title}--{content.director}--{content.year}--' \
              f'{content.genre}'
    with open(file, 'a') as f:
        f.write(str(content) + '\n')
    return True


def search_film(content):
    with open(file, 'r') as f:
        result = []
        for line in f:
            if content in line:
                res = line.split('--')
                result.append(res)
        if result == []:
            return ''
        else:
            return result


if __name__ == '__main__':
    print('Please use film_archive.py to start the app')