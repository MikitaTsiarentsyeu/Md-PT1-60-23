text_string = input('Пожалуйста, введите строку текста на русском: \n').lower()
#можно так
total = [+ 1 for i in range(len(text_string)) if text_string[i] in 'уеёаоэяиюы']
print('В вашей строке', len(total), 'гласных')
#можно так
#total = 0
#for i in range(len(text_string)):
    #if text_string[i] in 'уеёаоэяиюы':
        #total += 1
#print('В вашей строке', total, 'гласных')

