s = int (input ("Введите число больше 35 \n"))
while True:
    if s <= 35:
        print (' Неверное число')
    else:
        break
print ('Принято')    

with open ("D:/Гомолинская/Md-PT1-60-23/Tasks/Gomolinskaya/Task 4/text.txt", "r", encoding = 'utf-8') as f:
    for line in f:  
        count = 0
        row_size = len(line)
        with open ("D:/Гомолинская/Md-PT1-60-23/Tasks/Gomolinskaya/Task 4/n_text.txt", "a" , encoding = 'utf-8') as n:
            chunk = int(s)
            for line in line:
               n.write(line[count:row_size] + '\n')
               for text in line:
                 count += 1
                 all = ('\t'.join(text.split(' ')))
                 if count + chunk > row_size:
                     n.write('{:>35}'.format(line.strip()))  
                     count += 1
            out= [' '.join(line.split()) for line in line]
            n.write('\n'.join(out))
