def summa(a, b):
    return int(a) + int(b)

while True:
    z,c = input(),input()
    try:
        z,c ==int(z),int(c)
        print(summa(z,c))
    except ValueError:
        print("Не число!")
