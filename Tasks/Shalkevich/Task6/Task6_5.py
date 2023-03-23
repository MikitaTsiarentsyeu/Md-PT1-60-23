def fibo(nombers):
    if nombers < 2:
        return nombers
    else:
        return fibo(nombers - 1) + fibo(nombers - 2)

while True:
    nomb = int(input(" Ну что... Фибоначи?) Ведите число"))
    print(fibo(nomb))