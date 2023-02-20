n = int(input("Please, put your number of characters in the string that is at least 36:\n"))

with open("text.txt", 'r', encoding='utf-8') as f:
    text = f.read()

with open("new_text.txt", 'w') as new:
    string = ''
    string_1 = ''
    c = 0
    for i in text.split():
        c += len(i)
        if c >= n:
            string += "\n"
            c = len(i)
        elif string != '':
            string += ' '
            c += 1
        string += i
    for i in string.split("\n"):
        a = n - len(i)
        while a > 0:
            i = i.replace(' ','  ',a)
            a = n - len(i)
        string_1 += i
        string_1 += "\n"
    new.write(string_1)