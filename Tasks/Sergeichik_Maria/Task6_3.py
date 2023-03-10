def tocount (str, char, count = 0):

    if str[0] == char:
        count += 1

    if len(str) == 1:
        return count

    return tocount (str[1:len(str)], char, count)

    
   

word = input("Введите произвольное слово:\n")
symbol = input("Введите подсчитываемый символ:\n")

print(tocount(word, symbol))

