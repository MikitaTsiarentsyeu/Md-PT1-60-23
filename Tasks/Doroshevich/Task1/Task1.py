import math
start_amount = float(input("Enter the deposit amount:\n"))
time = float(input("Enter the term of the deposit (number of years):\n"))
percent = float(input("Enter interest rate:\n"))

final_amount = start_amount + start_amount*time*percent/100
final_amount = str(round(final_amount, 2)).split(".")
rubles = final_amount[0]
pennies = final_amount[1]

if time == 1 and int(pennies) == 1:
    print("The amount of your contribution after", time,
          "year will be:", rubles, "rubles", pennies, "penny")
elif time != 1 and int(pennies) == 1:
    print("The amount of your contribution after", time,
          "years will be: ", rubles, "rubles", pennies, "penny")
elif time == 1 and int(pennies) != 1:
    print("The amount of your contribution after", time,
          "year will be: ", rubles, "rubles", pennies, "pennies")
else:
    print("The amount of your contribution after", time,
          "years will be: ", rubles, "rubles", pennies, "pennies")
