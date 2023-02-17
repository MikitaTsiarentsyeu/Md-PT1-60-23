while True:
    string = input('Enter something\n')
    vowels_eng, vowels_rus  = "aeiouyAEIOUY", "АаЕеЁёИиОоУуЭэЮюЯяЫы"
    count_eng = 0
    count_rus = 0
    if string == '' or string == ' ':
        print('The string is empy, try again please!')
        continue
    for vwls in string:
        if vwls in vowels_eng:
            count_eng += 1
            print(f'I found ENGLISH vowel {[vwls]}')
        elif vwls in vowels_rus:
            count_rus += 1
            print(f'I found RUSSIAN vowel {[vwls]}')
    print(f'As result I found {count_eng} english vowels and {count_rus} russian vowels.')
    choice = input('Do you wanna play again?\n'
                   'Enter "1" to play again, "2" to exit\n ')
    if choice == '1':
        continue
    else:
        print('Good luck, have fun')
        break