import logik

def add_newRecord():
    biblio_data = input("Enter title, artist/director, year, genre separated by spaces\n")
    biblio_data = list(biblio_data.title().split())
    logik.add_newRecord(biblio_data)

def list_allAlbums():
    read = logik.list_allAlbums()
    print(read)

def search_by(gener):
    try:
        name = input("Enter search word:\n")
        name = name.title()
        while True:
            for i in gener:
                if name in i:
                #result = next(item)
                    print(f"{next(gener)}\n")#f"title: {result["title"]}, artist: {result["artist/director"]}, year: {result["year"]}, genre:{result["genre"]}")
            else:
                next(gener) 
    except StopIteration:
        print("Nothing found!")            

def main_cycle():
    while True:
        print("\nSelect an item from the menu:")
        print("\n1. Add new record\n2. List all albums\n3. Search for an album or movie\n4.Exit.")
        answer = input()
        if answer == "1":
            add_newRecord()
        elif answer == "2":
            list_allAlbums()
        elif answer == "3":
            print("\nSelect an item to search:")
            print("\n1.Serch by title\n2.Serch by artist/director\n3.Serch by year\n4.Serch by genre")
            answer2 = input()
            if answer2 == "1":
                search_by(logik.search_title())
            elif answer2 == "2":
                search_by(logik.search_artist())
            elif answer2 == "3":
                search_by(logik.search_year())
            elif answer2 == "4":
                search_by(logik.search_genre())
            else:
                break    
        elif answer == "4":
            break
        
if __name__ == "_main_":
    main_cycle()        
