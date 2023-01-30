deposit=float(input("Введите начальную сумму депозита: "))
percent=float(input("Введите процентную ставку: "))
periodicity=float(input("Сколько раз учитывается процентная ставка за год: "))
years=int(input("Введите срок вклада в годах: "))

result=float(deposit*(1+(percent/100)/periodicity)**(periodicity*years))
result=round(result, 2)

print(result)
