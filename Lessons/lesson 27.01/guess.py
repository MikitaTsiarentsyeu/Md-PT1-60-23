import random

my_number = random.randint(0, 10)

your_number = int(input("Guess the number:\n"))

if my_number == your_number:
    print("Correct!")
else:
    print("Loooooooser!")