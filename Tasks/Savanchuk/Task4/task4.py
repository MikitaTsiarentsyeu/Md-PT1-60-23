while True:
    answer = input("Введите максимальное количество символов в строке, которое больше 35:\n ")
    if not answer.isdigit():
        print("Введите число!")
        continue
    a = int(answer)
    if a <= 35:
        print("Число должно быть больше 35!") 
        continue
    break   
with open("text.txt", 'r', encoding='utf-8' ) as f:
    line = f.read()
with open ("new_text.txt", 'w', encoding='utf-8') as new:
    text = ''
    counter = 0
    # for i in line:
    #     counter +=1  
    #     if counter <= a:
    #         text += i 
    #     if counter == a:
    #         text += '\n'
    #         counter = 0
    # texts = text.split('\n')  
    for i in line.split():
        counter += len(i) # !)считаю символы в словах
        if counter >= a: # 2)если слово вмещается в строку 
            text += '\n'   # если слово не вмещается в строку ставлю перенос
            counter =  len(i)  # считаю кол-во символов в слове, кот. не вместилось, затем 5)
        elif text != '':    
            text += ' '     # 3) ставлю пробел после слова
            counter += 1   # 4) добавляю в счетчик пробел после слова
        text += i        # 5) Добавляю слово в строку
    for i in text.split('\n'):  
        x = a - len(i)      # считаю сколько пробелов необх. добавить
        while x > 0:         
            i = i.replace(' ','  ', x)  #меняю 1 прбел на 2
            x = a - len(i)  #если остается место, добавляю еще 1 пробел 
        text = i + '\n'  
        new.writelines(text)       

        





   