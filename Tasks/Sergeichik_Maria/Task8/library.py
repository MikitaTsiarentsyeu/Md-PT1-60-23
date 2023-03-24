import users
import logic
import csv

if __name__ == "__main__":

    with open(logic.FILENAME, 'a', newline='') as file:
            columns = [logic.nameKey, logic.producerKey, logic.yearKey, logic.genreKey]
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            
    users.main_cycle()