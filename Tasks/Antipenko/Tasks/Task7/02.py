'''Write a function that reads a file and returns its contents as a string.
Handle the FileNotFoundError and return "File not found" if the file does not exist.'''

def readfile(file):
    try:
        with open(file) as f:
            print(f.read())
    except FileNotFoundError:
        print('File Not Found :(')

readfile('file.txt')