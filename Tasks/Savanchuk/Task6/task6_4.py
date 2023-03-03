# Рекурсия возведения в степень
def exponentiation(a, n):
    if n == 1:     #условие, "а" в степени 1 - само число
        return a
    return a * exponentiation (a, n-1)   #вывожу произв числа на эту же функцию, в кот степень, уменьш на 1
print(exponentiation(2, 4))