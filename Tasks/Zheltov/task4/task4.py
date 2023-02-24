while True:
    simbol = input('введите количество символов в строке, больше 35: \n')

    if not simbol.isdigit():
        print("не, нужны числа а не буквы")
        continue

    if int(simbol) <= 35:
        print("ну вот опять, число должно быть больше 35!!")
        continue
    break
print('все, посмотрите этот файл и убедитесь finel.txt')
with open(r"C:\Users\saha2\OneDrive\Рабочий стол\IT-Academy\Md-PT1-60-23\Tasks\Zheltov\task4\text.txt", 'r', encoding = 'utf-8') as f:
    for line in f:
        offset = 0
        size_line = len(line)

        with open(r"C:\Users\saha2\OneDrive\Рабочий стол\IT-Academy\Md-PT1-60-23\Tasks\Zheltov\task4\finel.txt", 'a') as new:
            chunk = int(simbol)
            while offset+chunk < size_line:
                while line[offset+chunk] != chr(32):
                    chunk -= 1
                new.write((' ' * (int(simbol) - chunk - 1)) + line[offset:offset+chunk] + '\n')
                offset += chunk
                chunk = int(simbol)
            new.write(line[offset:size_line] + '\n')        