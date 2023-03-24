'''
1. Подготовиться к чтению содержимого файла text.txt
2. Дать пользователю ввести с клавиатуры условный параметр "максимальное количество символов в строке",
который должен быть больше 35
3. Отформатировать текст с учётом максимального количества символов, при этом
если слово целиком не умещается в строке, оно должно быть перенесено на следующую,
а отступы между словами равномерно увеличены (по аналогии с функцией "Выровнять по ширине" текстовых редакторов)
4. Записать получившийся текст в новый файл и оповестить об этом пользователя.
(модуль textwrap использовать нельзя)
'''

while True:
    am = input("Input the amount of characters per line(min - 36):\n")
    if int(am) > 35 and am.isnumeric():
        am = int(am)
        break
    else:
        print("Wrong input. Please try again.\n")

with open("text.txt", 'r', encoding='utf-8') as f:
    origin_text = f.read()
    formatted_text = ''
    formatted_line_counter = 0
    for i in origin_text.split():
        formatted_line_counter += len(i)
        if formatted_line_counter >= am:
            formatted_text += '\n'
            formatted_line_counter = len(i)
        elif formatted_text != '':
            formatted_text += ' '
            formatted_line_counter += 1
        formatted_text += i

with open("format_text.txt", 'w', encoding='utf-8') as form:
    for string in formatted_text.split('\n'):
        diffr = am - len(string)
        while diffr > 0:
            string = string.replace(' ', '  ', diffr)
            diffr = am - len(string)

        formatted_string = string + '\n'
        form.writelines(formatted_string)
