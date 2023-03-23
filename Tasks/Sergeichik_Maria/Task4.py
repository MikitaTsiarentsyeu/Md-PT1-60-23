symbols = input("Введите количество символов:\n")
symCount = int(symbols)
indexCursos = 0
result = ""

with open("test.txt", 'r', encoding='utf-8') as f : 
    while True:
        f.seek(indexCursos)
        fragment = f.read(symCount)
        index = symCount - 1
        emptyElementsCount = 0

        if len(fragment) < symCount:
            result += fragment
            break

        if len(fragment) < symCount:
            index = len(fragment) - 1

        for x in range (index, 0, -1):
            if fragment[x] == " ":
                indexCursos += x + 1
                break
            else:
                 fragment = fragment[:x] + ' ' + fragment [x + 1:]
                 emptyElementsCount += 1

        fragment = fragment.rstrip()
        words = fragment.split(" ")
        newFragment = ""
        if len(words) > 1:
            for i in range(len(words)):
                newFragment += words[i] + " " * (int)(emptyElementsCount / (len(words) - 1) + 1)

        result += newFragment + "\n"


with open("test1.txt", 'w', encoding='utf-8') as newF : 
    newF.write(result)


