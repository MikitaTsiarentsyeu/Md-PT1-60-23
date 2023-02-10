answer = input("Введите числа через пробел:\n")
sum = 0
for i in answer.split(): # вычленяет числа по пробелу
    if i.isdigit(): #проверка на числа
        if int(i) % 2 == 0:
            sum += int(i)
            print(sum) 
    else:
        ("Некорректный ввод!")