#Write a function that reads a file and returns its contents as a string. Handle the FileNotFoundError 
#and return "File not found" if the file does not exist.
file = "text.txt"
def file_read():
    try:
        with open(file, 'r') as f:
            line = f.read()
        return ''.join([i for i in line.split()]) + "\n"
    except FileNotFoundError:
        print("File not found")
file_read()

