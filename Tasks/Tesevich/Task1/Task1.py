a1 = int(input("Процент годовых\n"))
b = int(input("Количество лет\n"))
c = int(input("Сумма депозита\n"))
d = int(input("Частота перерасчета\n"))
a = float(a1*0.01)
e = round(c*(1+a/d)**(d*b))
print(("Итоговая сумма за ")+ str(b)+(" лет: ")+ str(e))