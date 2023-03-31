user_numb = input("Please, type any natural numbers in format 'a b c d e f':\n").split()

numbers = []
                                           # 12 16 55 87 41 2 3 6 58 4 122 99 54 58 51
for e in user_numb:
    if e.isdigit():
        numbers.append(int(e))

print("The average of all numbers in the list is:", float(sum(numbers)/len(numbers)))



