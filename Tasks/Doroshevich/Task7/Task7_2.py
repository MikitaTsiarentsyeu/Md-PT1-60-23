def file_to_str():
    try:
        with open('a.txt', 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "File not find"


print(file_to_str())
