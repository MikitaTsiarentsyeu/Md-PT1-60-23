with open("text.txt", 'r') as f:
    while True:
        n = input("Select the number of characters per line(min - 36):")
        if n.isnumeric() and int(n) > 35:
            n = int(n)
            break
        else:
            print("Wrong data. Please try again.")
    with open(f"text_{n}_symbols.txt", 'w') as new:
        for line in f:
            while len(line) > n:
                if line[n] == ' ':
                    s = line[:n]
                    line = line[n:].lstrip()
                    new.write(s + "\n")
                elif line[n-1] == ' ':
                    s = line[:n-1].split()
                    line = line[n:]
                    s[0] += ' '
                    s = ' '.join(s)
                    new.write(s + "\n")
                else:
                    s = line[:n].split()[:-1]
                    i = 0
                    j = 0
                    while i < len(line[:n].split()[-1]) + 1:
                        if j >= len(s) - 1:
                            j = 0
                        s[j] += ' '
                        i += 1
                        j += 1
                    s = ' '.join(s)
                    new.write(s + "\n")
                    line = line.replace(' '.join(s.split()), '').lstrip()
                if len(line) <= n:
                    new.write(line)
                    continue
    print(f"your formatted text is in a file: 'text_{n}_symbols.txt'")
