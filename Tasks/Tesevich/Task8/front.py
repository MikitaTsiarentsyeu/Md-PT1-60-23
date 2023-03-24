import back

def continue_funk():
    print("Return to main menu? y/n")
    dis = input()
    if dis == "y":
        main_men()
    else:
        pass



def main_men():
    print('Select a menu item:\n1. Browse all films\n2. Add new\n3. Search\n4. Exit')
    
    answer = input()
    if answer == '1':
        inf = back.data_reader()
        if inf == None:
            print("No films in vault\n")
            pass
        else:
            print('Your films:')
            for i in inf:
                print(f'Title: {i[0]}, Artist: {i[1]}, Year: {i[2]}, Genre: {i[3]}')
        continue_funk()
               
    elif answer == '2':
        print('\nEnter the title, without using "~"')
        title = input()
        if title.count('~')>=1 or title == " " or title == "":
            error_input()
                      
        print('Enter the artist, without using "~"')
        artist = input()
        if artist.count('~')>=1 or artist == " "  or artist == "" :
            error_input()

        print('Enter the year, without using "~"')
        year = input()
        if year.count('~')>=1 or year == " " or year == "":
            error_input()    
        print('Enter the genre, without using "~"')

        genre = input()
        if genre.count('~')>=1 or  genre == " " or genre == "":
            error_input()    
        
       
        else:   
            back.data_writer(title,artist,year,genre)
            print(f'\nYou add Title: {title}, Artist: {artist}, Year: {year}, Genre: {genre}')
            continue_funk()

    elif answer == '3':
        print('\nSelect a variant of searching:\n1. By title\n2. By artist\n3. By year\n4. By genre')
        answer_2 = input()
        if answer_2 == "1":
            search_by(back.search_title())
        elif answer_2 == "2":
            search_by(back.search_artist())
        elif answer_2 == "3":
            search_by(back.search_year())
        elif answer_2 == "4":
            search_by(back.search_genre())
        else:
            error_input()
    
    elif answer == '4':
        pass
    
    else:
        error_input()
         


def error_input():
    print('\nIncorrect input, try again\n')
    continue_funk() 
    
def search_by(ik):
    print('\nEnter the search word:')
    input_name = input()
    flag = 0
    for serch_name in ik:
        if input_name  in serch_name:
            find = next(ik)
            print(f'Title: {find[0]}, Artist: {find[1]}, Year: {find[2]}, Genre: {find[3]}')
            flag =1
        else: 
            next(ik)
    
    if flag ==0:
        print('\nNothing found')
        continue_funk()
    if flag>=1:
        continue_funk()
        
            
main_men()