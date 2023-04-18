while True:
    n = input("Select the number of characters per line(min - 36):\n")
    if n.isnumeric() and int(n) > 35:
        n = int(n)
        break
    else:
        print("Wrong data. Please try again.\n")

with open("text.txt", 'r') as f:
    with open(f"text_{n}_symbols.txt", 'w') as new:
        for line in f:
            result = ''
            while len(line) > n:
                if line[n] == ' ':
                    result = line[:n] + '\n'
                    line = line[n:].lstrip()
                elif line[n-1] == ' ':
                    s = line[:n-1].split()
                    line = line[n:]
                    s[0] += ' '
                    result = ' '.join(s) + '\n'
                else:
                    s = line[:n].split()[:-1]
                    stub = line[:n].split()[-1]
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

                if len(line) <= n:
                    result = line
                new.write(result)
    print(f"your formatted text is in a file: 'text_{n}_symbols.txt'")
