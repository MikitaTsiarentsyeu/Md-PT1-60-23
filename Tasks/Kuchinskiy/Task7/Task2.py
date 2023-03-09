
try:
    with open('test.txt', 'r', encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError as e:
    print("File not found")
    print(e)
else:
    print('file read successfully')