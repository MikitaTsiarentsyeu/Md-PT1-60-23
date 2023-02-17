print('Hello, dude. I can add all even numbers from your list.\n'
    'If you wanna see my power, press "1", or "2" to exit:(')
choice = input()
while choice == '1':
    l = input('enter numbers with _space_ between each others, please!\n')
    if l == '' or l == ' ':
        print('I can work only, if you enter some numbers..')
        continue
    if not ' ' in l:
        print('I NEED _SPACE_ between numbers, please !')
        continue
    l = map(int, l.split())
    sum = 0
    for i in l:
        if(i % 2) == 0:
            sum += i
    print(f'The result of all added even numbers are {sum}')
    repeat = input('How about to play again ?\n'
                   'Press "1" to play again, "2" to exit\n')
    if repeat == '1':
        continue
    else:
        break
else:
    print('Maybe next time? Goodbye!')