#(Напишите функцию, которая принимает на вход список
 #целых чисел и возвращает сумму всех четных чисел в списке.
#Обработайте TypeError и верните «Недопустимый тип ввода», 
#если ввод не является списком или не каждый элемент имеет тип int.)     
def func(*a):
    try:
        if len(a) <= 1:
            raise TypeError("Invalid input type") 
        res = 0
        for i in a:
            if not i.isdigit():  #if not isinstance(i, int)
                raise TypeError("Invalid input type")
            if int(i) % 2 == 0:
                res += int(i) 
        return res
    except TypeError as e:
        print(e)
a = input("Enter a list of integers:\n")
a = list(a.split())
print(func(*a))


