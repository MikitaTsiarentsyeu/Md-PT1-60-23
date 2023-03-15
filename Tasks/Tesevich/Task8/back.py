def data_reader():
    try:
        with open ('storage.txt', 'r') as storage_can:
            inf = []
            for line in storage_can:
                inf.append(line.rstrip().split('~'))
            return inf
    except FileNotFoundError:
        return None    

def data_writer(title,artist,year,genre):
    with open ('storage.txt', 'a') as storage_can:
        storage_can.write(f'{title}~{artist}~{year}~{genre}\n') #использую знак ~ как разделитель так как подобное редко пользуется в названиях
        
        

def search_title():
    titles = data_reader()
    for i in titles:
        yield i[0]
        yield i

def search_artist():
    titles = data_reader()
    for i in titles:
        yield i[1]
        yield i

def search_year():
    titles = data_reader()
    for i in titles:
        yield i[2]
        yield i

def search_genre():
    titles = data_reader()
    for i in titles:
        yield i[3]
        yield i