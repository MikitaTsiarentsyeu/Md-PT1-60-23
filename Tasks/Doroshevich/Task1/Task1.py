import math
start_amount = int(input("Введите сумму вклада в рублях:\n"))
time = int(input("Введите срок вклада(количество лет):\n"))
percent = int(input("Введите процентную ставку:\n"))

final_amount = start_amount + start_amount*time*percent/100

if time % 10 == 1 and time % 100 != 11:
    print("Сумма Вашего вклада через", time,
          "год составит: " + str(final_amount) + "BYN")
elif 1 < time % 10 < 5 and time % 100 not in range(12, 15):
    print("Сумма Вашего вклада через", time,
          "года составит: " + str(final_amount) + "BYN")
else:
    print("Сумма Вашего вклада через", time,
          "лет cоставит: " + str(final_amount) + "BYN")
