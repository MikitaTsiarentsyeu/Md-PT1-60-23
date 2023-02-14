print("Добро пожаловать в нашу прекрасную библиотеку и не важно, что книга у нас одна.. ЗАТО КАКАЯ!!\n"
"Но перед прочтением выберете сколько символов должно быть в строе. ЭТО ВАЖНО!!")
while True:
    p = input()
    try:
        p = int(p)
        if p >=35:
            break
        else:
            print("Надо от 35 строк. Оно того стоит. Я тебе отвечаю!")
    except ValueError:
        print("ЭТО ВАЖНО!!!")
        continue
with open('text.txt', 'r', encoding='utf8') as f:
    line = f.readlines()
with open('Task4.txt', 'w', encoding='utf8') as f:
    text = " "
    counter = 0
    for i in line:
        for j in i.split():
            new_count = counter + len(j)
            if counter != 0:
                new_count += 1
            if new_count >= p:
                text += "\n"
                counter = 0
            if counter != 0:
                text += ' '
                counter += 1
            text += j
            counter += len(j)
    texts = text.split('\n')
    for l in texts:
        c = l.count(' ')
        if len(l) < p and c != 0:
            final = (p - len(l)) // c
            surplus = (p - len(l)) % c
            if final > 0:
                l = l.replace(' ', ' ' + ' ' * final)
            if surplus > 0:
                l = l.replace(' ' + ' ' * final, ' ' + ' ' * final + ' ', surplus)
        l = l + '\n'
        f.writelines(l)

file = open('Task4.txt', encoding='utf - 8')
print(file.read())
file.close()