import csv

def get_all_movies():
    with open("movies.csv", 'r', encoding = 'utf-8') as f:
        file_reader = csv.DictReader(f, delimiter = ",")
        title = '\n'.join([f'{row["title"]}' for row in file_reader])
        return f'List of movies: \n{title}'

def add_new_movie(*args):
    with open("movies.csv", 'a', newline = '') as f:
        file_writer = csv.writer(f, delimiter = ",")
        file_writer.writerow([*args])


def search_movie(keys, inp):
    with open("movies.csv", 'r', encoding = 'utf-8') as f:
        file_reader = csv.DictReader(f, delimiter = ",")
        list_of_dict = (row for row in file_reader) # generator expressions
        search_output = []
        for key in list_of_dict:
            if key.get(keys) == inp:
                search_output.append(f'{key["title"]}: {key["year"]}, {key["genre"]}')
        return '\n'.join(search_output)

