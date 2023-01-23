import math
m= int (input ("Введите сумму денежных средств для хранения в банке: \n"))
y = int(input("Введите срок хранения денежных средств (в годах):\n"))
p =  float (input("Введите процент:\n"))
year=y*12
procent= p/100
bank=m*(1+procent/year)**(year*y)
print("Ваш счет после истечения срока:\n")
print("%.2f" % bank )
#print("\n")
print("Спасибо, что выбрали нас :)\n")







