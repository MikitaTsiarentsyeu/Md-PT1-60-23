def power(number, degree):
    if (degree == 1):
        return (number)
    if (degree != 1):
        return (number * power(number, degree - 1))
    
number = int(input("Введите число: "))

degree = int(input("Введите степень: "))
print("Результат возведения в степень:", power(number, degree))