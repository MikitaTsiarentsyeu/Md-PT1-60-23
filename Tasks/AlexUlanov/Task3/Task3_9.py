#9. Write a program that takes a string as input and returns the string reversed.

a="Речь Посполи́тая (польск. Rzeczpospolita, з.-рус. Рѣч Посполита) — конфедеративное государство"

rez=""
for i in range (0, len(a)):
    rez+=(a[len(a)-i-1]) 
            
print(rez)