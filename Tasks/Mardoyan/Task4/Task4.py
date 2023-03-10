chunk = int(input('Input your quantity of symbols, but quantity must be more then 35 symbols.\n'))
while True:
    if chunk > 35:
        break
    else:
        chunk = int(input('Incorrect value!Quantity must be more then 35 symbols.\n'))
with open("text.txt", 'r') as f:
    with open("new_text.txt", 'w') as new:
        for line in f:
            result = ''
            while len(line) > chunk:
                if line[chunk] == ' ':
                    result = line[:chunk] + '\n'
                    line = line[chunk:].lstrip()
                elif line[chunk-1] == ' ':
                    s = line[:chunk-1].split()
                    line = line[chunk:]
                    s[0] += ' '
                    result = ' '.join(s) + '\n'
                else:
                    s = line[:chunk].split()[:-1]
                    stub = line[:chunk].split()[-1]
                    line = line.replace(' '.join(s), '').lstrip()
                    i = 0
                    j = 0
                    while i < len(stub) + 1:
                        if j >= len(s) - 1:
                            j = 0
                        s[j] += ' '
                        i += 1
                        j += 1
                    result = ' '.join(s) + '\n'

                if len(line) <= chunk:
                    result = line
                new.write(result)

                

        

        