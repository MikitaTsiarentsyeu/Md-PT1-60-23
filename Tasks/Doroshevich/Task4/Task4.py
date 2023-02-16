with open("text.txt", 'r') as f:
    while True:
        n = input("Select the number of characters per line(min - 36):\n")
        if n.isnumeric() and int(n) > 35:
            n = int(n)
            break
        else:
            print("Wrong data. Please try again.\n")
    with open(f"text_{n}_symbols.txt", 'w') as new:
        for line in f:
            while len(line) > n:
                # if the last character is at the end of a word
                if line[n] == ' ':
                    s = line[:n]
                    line = line[n:].lstrip()
                    new.write(s + "\n")
                # if the last character is a space
                elif line[n-1] == ' ':
                    s = line[:n-1].split()
                    line = line[n:]
                    s[0] += ' '
                    s = ' '.join(s)
                    new.write(s + "\n")
                # if the character divides word
                else:
                    s = line[:n].split()[:-1]
                    stub = line[:n].split()[-1]
                    line = line.replace(' '.join(s), '').lstrip()
                    i = 0
                    j = 0
                    # add spaces, in the amount of the length of the cut piece of the word +1
                    while i < len(stub) + 1:  
                        # if we need to go to the 2nd round
                        if j >= len(s) - 1:                  
                            j = 0
                        s[j] += ' '
                        i += 1
                        j += 1
                    s = ' '.join(s)
                    new.write(s + "\n")
                
                if len(line) <= n:
                    new.write(line)
                    continue
    print(f"your formatted text is in a file: 'text_{n}_symbols.txt'")
