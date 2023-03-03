#Сразу извиняюсь)Знаю,что написано бредово,но я очень старался!Потом рад буду выслушать твои советы)

user_input = input('Please input ordered list of numbers without duplicates tgrought "Space"\n')
#Превращаю инпут в Int
user_input = user_input.split(' ')
data = []
for i in user_input:
    data.append(int(i))


def range_func(a):
    c = 0
    d = [] #Список со списками(разделил каждый range)
    z = [] #Список для каждых последующих эл.
    g = [] #С диапазонами
    #В цикле ставим 2 условия,если след. эл. больше на 1 ,то подходит и мы добавляем в список
    for i in range(len(a)-1):
        if a[c] - a[c+1] == -1:
            z.append(a[c])
            c += 1
        elif a[c] - a[c+1] != -1: #Если же не подходит,идет разветвление для одиночных элементов и последующих,которые встречаются далее
            if a[c] - a[c+1] != -1 and a[c] - a[c-1] != 1:
                d.append(a[c])
                z = []
                c +=1
            elif a[c] - a[c+1] != -1:
                z.append(a[c])
                d.append(z)
                z = []
                c +=1   
            elif a[c] == a[-1] and a[c] - a[c-1] != 1:
                d.append[a[c]] #Условие ,если цифра в конце одиночная     
    d.append(a[c])
    for i in d:
        if type(i) == list: #Разделение,чтобы слепить все
            q = f'{min(i)} - {max(i)}'
            g.append(q)
        else:
            g.append(i)
    return g


print(range_func(data))
    
        

