import csv
def add_a_new_movie(*args):
    with open("store.csv",'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(args)

def get_all_movies():
    with open("store.csv", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield (f"title: {row['title']}, director: {row['director']}, year: {row['year']}, genre: {row['genre']}")
       

def search(item):
     with open("store.csv", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if item in row.values():
                yield(f"title: {row['title']}, director: {row['director']}, year: {row['year']}, genre: {row['genre']}")
            


