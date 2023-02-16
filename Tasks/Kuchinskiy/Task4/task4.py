inp = int(input('enter numb\n'))
while True:
    if inp < 35:
        inp = int(input('once more\n'))
    else:
        break

with open("new_text.txt", 'w') as new:
    new.write('') # обнуляем файл

with open("text.txt", 'r') as f:
    for l in f:
        with open("new_text.txt", 'a') as new:
            s_max = inp
            sh = 0 # позиция курсора
            while sh <= len(l)-1: # пока курсор не дойдет до последнего элемента сроки
                flag = True 
                if len(l[sh:len(l)-1]) > s_max: # проверка на кол-во символов чтобы было больше введеного значения
                    while flag:
                        if l[s_max + sh]!=' ': # тут есть пробел?
                            s_max = s_max - 1 # убираем длину символов пока не найдем пробел
                            space = inp - s_max # счетчик пробелов
                        else:
                            flag = False # как только нашли пробел переключили флажок
                    g = l[sh:s_max + sh].split() # сплитуем кусок строки чтобы добавить пробелы
                    it = 1 
                    while it != space + 1: # цикл добавления пробелов
                        for i in range(len(g)-1): # пробегаемся по куску строки
                            if it <= space:  # добавляем если нужно
                                g[i] = g[i] + ' ' 
                                it += 1 # и считаем сколько добавили
                            else:
                                break
                    g = ' '.join(g)
                    new.write(g +'\n') 
                else:
                    new.write(l[sh:]) # запись оставшегося куска
                sh = sh + s_max + 1 # сдвигаем курсор на длину строки + пробел
                s_max = inp # перезаливаем s_max на введенное значение пользователя
                space = 0  # обнуляем счетчик пробелов
print('you have written the formatted text to a new file')
