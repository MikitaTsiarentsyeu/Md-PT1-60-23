def reading_file():
    with open("Test.txt", 'r', encoding = 'utf-8') as f:
        print(f.read)

try:
    reading_file()
except FileNotFoundError:
    print('File not found')