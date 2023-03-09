def ReadFile():
    try:
        with open ("text.txt", "r", encoding="utf-8") as f:           
            return print(f.read())
    except:
        print("File not found")

        return False

ReadFile()