user_numb = input("Please, type any numbers in format 'a b c d e f':\n").split()

numbers = []
even_numb = []

for e in user_numb:
    if e.isdigit():
        numbers.append(int(e))

for num in numbers:
    if num % 2 == 0:
        even_numb.append(num)

print(sum(even_numb))

