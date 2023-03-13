def file_read(file):
    try:
        with open(file, 'r') as f:
            return f.read()
        
    except FileNotFoundError:
        print("File not found")
print(file_read("tex.txt"))


