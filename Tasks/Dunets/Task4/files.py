while True:
    x = input('Введите длину строки, больше 35:\n')

    if not x.isdigit() or int(x) <= 35:
        print('Пожалуйста, попробуйте еще раз')
    else:
        x = int(x)
        break

with open("text.txt", 'r') as f:
    with open('new_txt.txt', 'w') as new:
        for line in f:
            new_text = ''
            while len(line) > x:
                # if the last character is at the end of a word
                if line[x] == ' ':
                    new_text = line[:x] + '\n'
                    line = line[x:].lstrip()
                # if the last character is a space
                elif line[x - 1] == ' ':
                    list = line[:x - 1].split()
                    line = line[x:]
                    list[0] += ' '
                    new_text = ' '.join(list) + '\n'
                # if the character divides word
                else:
                    list = line[:x].split()[:-1]
                    edge = line[:x].split()[-1]
                    line = line.replace(' '.join(list), '').lstrip()
                    # add spaces, in the amount of the length of the stub + 1
                    a = 0
                    b = 0
                    while a < len(edge) + 1:
                        # if we need to go to the 2nd round
                        if b >= len(list) - 1:
                            b = 0
                        list[b] += ' '
                        a += 1
                        b += 1
                    new_text = ' '.join(list) + '\n'

                if len(line) <= x:
                    new_text = line
                new.write(new_text)
    print("Done!")



# te = 'one two three four five'
# t = te.split()[:-1]
# te = te.replace(' '.join(t), '').lstrip()
# print(te)
