# Вывести числа от 1 до n
def sequence (n):
    if n == 1:
        return 1
    return str(sequence(n-1)) + ' ' + str(n)
print(sequence (10))            #1 2 3 4 5 6 7 8 9 10

def num(a:int, b:int):
    if a < b:
        if a == b:
            return a
        return str(a) + ' ' + str(num(a+1, b)) 
    else:
        if a == b:
            return a
        return str(a) + ' ' + str(num(a-1, b))
print(num(10, 20))
