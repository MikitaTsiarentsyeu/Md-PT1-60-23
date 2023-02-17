while True:
    string = int(input('Enter a string length:\n'))
    if string <= 35:
        print('Too short..Need longer..')
        continue
    else:
        break

index = 0
with open('text.txt', 'r') as f:
    with open('new_text.txt', 'w') as x:
        counter = 0
        while True:
            counter += 1
            mean = True
            add_index_1 = 0
            add_index_2 = 0
            str_counter = 0

            f.seek(index)
            if f.read(1) == ' ':
                edit_string = f.read(string)
                index += 1
            else:
                f.seek(index)
                edit_string = f.read(string)

            f.seek(index)
            edit_string = f.read(string)
            last_index = string

            if not edit_string:
                break
            if '\n' in edit_string:
                last_index = edit_string.find('\n')
                add_index_1 += 2
                mean = False
            elif len(edit_string) >= 1 and edit_string[-1] == ' ':
                last_index = string - 1
            elif len(edit_string) <= string - 1:
                mean = False
            else:
                last_index = edit_string.rindex(" ")

            index += last_index + add_index_1
            edit_string = edit_string[0:last_index]

            string_counter = string - 1 - last_index + add_index_2

            while mean:
                for i in range(len(edit_string)-1, -1, -1):
                    if string_counter == 0:
                        mean = False
                        break
                    elif edit_string[i] == ' ':
                        string_counter -= 1
                        edit_string = edit_string[: i + 1] + edit_string[i:]

            x.write('\n' + edit_string) if counter != 1 else x.write(edit_string)

print('\nThe text saved to "new_text.txt".')