import math
n=int(input("Введите количество символов в строке (Более 35)\n"))
while True:  
    if n>35:
        break
    else:
        n=int(input("Неверное количество символов в строке (Введите число Более 35)\nВВОДИТЕ СНОВА\n"))

with open("text2.txt", 'w') as new:
    new.write('') 

with open ("text.txt", "r", encoding="utf-8") as f:
    for line in f:
        x=line                             
        x=x.split()
        with open ("text2.txt", "a", encoding="utf-8") as f:                
                s=0        
                WS=""                       
                flag=False
                d=0
                d1=0

                # Основной цикл:
                #1. Формируем строчку до n значений
                #2. Анализируем строчку сколько не хватает пробелов
                #3. Отправляем обратно строчку в список
                #4. Формируем строчку необходимой длины с необходимым количеством пробелов
                
                while True:                                       
                    if len(WS)+len(x[0])<n:
                        WS += "".join(x[0])
                        WS += " "                                
                        x.pop(0)

                        if len(x)==0:      # В этом блоке записываю остаток и выхожу из цикла.
                            f.write (WS)
                            f.write ("\n")
                            WS = ""
                            d=0
                            break

                        while (d>0 or d1>0):    # В этом блоке вставляются дополнительные пробелы
                            while d1>0:
                                WS += " "
                                d1-=1
                                break
                            for i in range(d):
                                WS += " "
                            break   

                    if len(WS) == n:         # Запись данных
                        f.write (WS)
                        f.write ("\n")
                        WS = ""
                        d=0
                                       
                    if len(WS)+len(x[0])>=n:   # Тут анализируется строка и считаем количество недостающих пробелов                                           
                        Buf=WS.split()
                        x=Buf+x    
                        s = n-len(WS)    # Для того чтобы понять сколько пробелов не хватает нужно собрать 1 строчку    
                        WS = ""
                        d = math.floor(s/len(Buf))           # Определим в среднем количество табуляций на 1 слово
                        d1 = s%len(Buf)             # Опледелим есть ли еще пробелы из остатка
                        
print("Ok")
                                 
                        


                    



                   
    


