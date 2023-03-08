def Libr (txt):
    try:
        open(txt)
    except FileNotFoundError:
        return print("File not found")

Libr(input("какую книгу вам открыть?"))
