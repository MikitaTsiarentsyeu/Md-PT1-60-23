#5. Write a program that takes a list of strings as input and returns a list with all strings that have a length greater than 5 characters.

string=["Речь Посполи́тая (польск. Rzeczpospolita, з.-рус. Рѣч Посполита) — конфедеративное государство", 
"Возникшее в результате объединения Королевства Польского и Великого княжества Литовского на основе Люблинской унии в 1569 году",
"на",
"от",
"и ликвидированное в 1795 году с разделом его земель между Российской империей, Пруссией и Австрией."]

for i in range (len(string)):
        if len(string[i])>5:
            print(string[i])
    





