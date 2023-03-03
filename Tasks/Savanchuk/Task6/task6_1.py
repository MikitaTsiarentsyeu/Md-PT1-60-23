#  Write a recursive function to reverse a string.
def reversed_str(a):
    if len (a) < 1:  #если длина строки < 1 симв, ф-я вызывает себя
        return a
    else:
        return reversed_str(a[1:]) + a[0]  # иду в обратную сторону, приклеивая к началу новой стр 1 эл с конца 
print(reversed_str(a = "Скоро весна. Солнце светит ярко."))