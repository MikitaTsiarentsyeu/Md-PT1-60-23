def recursion_count(text, i=0):
    if text == '':
        return f'Данный символ был использован {i} раз.'
    elif text.isalpha():
        return recursion_count(text[1:], i + 1)

print(recursion_count(text=input("Введите один символ(букву) н-ное количество раз:\n").replace(" ", "")))