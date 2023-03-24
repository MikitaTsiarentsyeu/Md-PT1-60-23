def reading(text):
    try:
        open(text)
    except FileNotFoundError:
        return print("File not found")

reading(input("Enter a book to read\n"))