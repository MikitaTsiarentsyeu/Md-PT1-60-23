def check(line, symbol):
    if not line:
        return 0
    elif line[0] == symbol:
        return 1 + check(line[1:], symbol)
    else: 
        return check(line[1:], symbol)
    
line = input("Введите строку:")

symbol = input("Введите букву для проверки:")

print("Количество вхождений:")
print(check(line, symbol))