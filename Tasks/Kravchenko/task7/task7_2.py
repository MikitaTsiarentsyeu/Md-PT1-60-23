# 2. Write a function that reads a file and returns 
# its contents as a string. Handle the FileNotFoundError 
# and return "File not found" if the file does not exist.

file_name = input('Enter a file name to open\n')
try:
    with open (file_name, 'r', encoding='utf-8') as file:
        content = " ".join([line.strip() for line in file.readlines()])
        print(content)
   
except FileNotFoundError:
    print("File not found")