import json


class Movie:
    def __init__(self, title, year, directors_name, genre):
        self.__title = title
        self.__year = year
        self.__directors_name = directors_name
        self.__genre = genre

    def get_title(self):
        return self.__title

    title = property(get_title)

    def get_year(self):
        return self.__year

    year = property(get_year)

    def get_directors_name(self):
        return self.__directors_name

    directors_name = property(get_directors_name)

    def get_genre(self):
        return self.__genre

    genre = property(get_genre)

    def record(self):
        dct = {
            'title': self.title,
            'year': self.year,
            'directors_name': self.directors_name,
            'genre': self.genre
        }
        return dct

    my_dct = property(record)


class RepoActions:

    @staticmethod
    def make_repo():
        dct = {'data': []}
        try:
            with open("repo.json", "w") as f:
                json_repo = json.dump(dct, f)
        except Exception:
            print("The repo is already exists")

    @staticmethod
    def write_to_repo(my_dct):
        try:
            with open("repo.json", 'r+') as file:
                file_data = json.load(file)
                file_data["data"].append(my_dct)
                file.seek(0)
                json.dump(file_data, file, indent=4)
        except Exception:
            print("Wrong format to append to the repo")

    @staticmethod
    def read_from_repo():
        try:
            with open("repo.json") as f:
                json_data = json.load(f)
                return json_data["data"]
        except Exception:
            return "Can't read the repo"

    @staticmethod
    def search(option, searched_str):
        option = option
        searched_str = searched_str
        for dct in RepoActions.read_from_repo():
            if searched_str in dct[option]:
                yield f"'{dct['title'].title()}': Directed by {dct['directors_name']}, {dct['year']}, {dct['genre']}"









