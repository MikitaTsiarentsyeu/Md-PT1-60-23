def openfile():   
    try:
        with open('text.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        return "File not found"
    
print(openfile())