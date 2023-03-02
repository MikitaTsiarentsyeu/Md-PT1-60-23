# Функция находит палиндром и выводит его
def palindrom (a):
    a = a.replace(' ', '').lower() #убираю пробелы и привожу к нижнему регистру
    res = ''
    for i in a.split('.'):
        if i == reversed_str(i):
            res += i
            res +='\n'
    return res

def reversed_str(i):
    if len (i) == 0:  #если длина строки - пустая строка, ф-я завершает свою работу
        return i
    else:
        return i[::-1]
print(palindrom(a = "Лёша на полке клопа нашёл. мама. Мадам.")) 


   #Write a function to check whether a given string is a palindrome. 
def palindrom (a):
    a = a.replace(' ', '').lower()
    if a == a[::-1]:
        return "Палиндром"
    else:
        return "Не палиндром"
print(palindrom (a = "Лёша на полке клопа нашёл"))        
 
   #Рекурсия
def palindrom(a):
    if len(a) < 1:  #условие рекурсии
        return True
    else:
        if a[0] == a[-1]:  #сравниваю первый эл и последний
            return palindrom(a[1:-1]) #вызываю ф-ю и сравниваю последущие эл
        else:
            return False
a = input("Enter string:\n")
if palindrom(a) == True:
    print("Данная строка палиндром.")
else:
    print("Данная строка не палиндром.")
     