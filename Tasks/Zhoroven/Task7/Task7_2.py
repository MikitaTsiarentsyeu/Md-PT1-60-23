def reader(file):
    try:
        f = open("text.txt", 'r')
        f.read()
    except FileNotFoundError:
        print("File not found")


reader("text.txt")
