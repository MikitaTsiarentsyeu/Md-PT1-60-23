while True:
    simbol = input('Введите, пожалуйста, количество символов в строке больше 35: \n')
    
    if not simbol.isdigit():
        print("Пожалуйста, вводите только числа")
        continue

    if int(simbol) <= 35:
        print("Вы ввели число меньше либо равное 35")
        continue
    break
print('Отлично! Можете посмотреть результат работы программы в файле Result.txt')

with open("text.txt", 'r', encoding = 'utf-8') as f:
    for line in f:
        offset = 0
        size_line = len(line)
        
        with open("Result.txt", 'a') as new:
            chunk = int(simbol)
            while offset+chunk < size_line:
                while line[offset+chunk] != chr(32):
                    chunk -= 1
                new.write((' ' * (int(simbol) - chunk - 1)) + line[offset:offset+chunk] + '\n')
                offset += chunk
                chunk = int(simbol)
            new.write(line[offset:size_line] + '\n')        