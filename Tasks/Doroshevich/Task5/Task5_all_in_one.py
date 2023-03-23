import random


def list_of_strings():
    print("Enter the number of strings:")
    while True:
        len_l = input()
        if len_l.isnumeric():
            return [input(F"Enter string №{x+1}\n") for x in range(int(len_l))]
            break
        else:
            print("Wrong data. Please enter integer!")


def func_sum():
    while True:
        term1, term2 = input("Enter 1st argument:\n"), input(
            "Enter 2nd argument:\n")
        if term1.isnumeric() and term2.isnumeric():
            return "Your result:\n" + f"{int(term1) + int(term2)}"
        else:
            print("Wrong data. Please enter integers!")


def reverse_string():
    return f"List of all reversed strings:\n{[x[::-1] for x in list_of_strings()]}"


def g5_strings():
    return f"list with all the strings that have a length greater than 5:\n{[x for x in list_of_strings() if len(x) > 5]}"


def low_up_case():
    s = input("Enter a string:\n")
    lower = len([x for x in s if x.islower()])
    upper = len([x for x in s if x.isupper()])
    return f"count of lower case symbols is {lower}\ncount of upper case symbols is {upper}"


def ranges_of_numbers():
    l = list(set([random.randint(0, 20) for i in range(20)]))
    print(f"Your ordered list of numbers without duplicates:\n{l}")
    l1 = [l[0]]
    for i in range(1, len(l)-1):
        if l[i] - l[i-1] == 1 and l[i+1] - l[i] == 1:
            l1 += ['']
        elif l[i] - l[i-1] == 1 and l[i+1] - l[i] != 1:
            l1 += [-l[i]]
        else:
            l1 += [', ', l[i]]
    l1 += [-l[-1]] if l[-1] - l[-2] == 1 else [', ', l[-1]]
    return f"Your string with ranges for those numbers:\n{''.join([str(x) for x in l1])}"


func = {'1': func_sum, '2': reverse_string, '3': g5_strings,
        '4': low_up_case, '5': ranges_of_numbers}
while True:
    print("Select a task number:\n1 - A function that takes two integers as arguments and returns their sum.\n2 - A function that takes a list of strings as an argument and returns a new list of strings that are all reversed.\n3 - A function that takes a list of strings as an argument and returns a new list with all the strings that have a length greater than 5.\n4 - A function that takes a string as an argument and returns two numbers, first for count of lower case symbols, second for count of the upper case symbols in the initial string.\n5 - A function that takes an ordered list of numbers without duplicates and returns a string with ranges for those numbers.")
    while True:
        choice = input()
        if choice.isnumeric() and 0 < int(choice) < 6:
            print(func[choice]())
            break
        else:
            print("Wrong data. Please enter a number from 1 to 5!")
    print("Do you want to complete another task?(enter 'y' if yes, 'n' if no)")
    while True:
        repeat = input()
        if repeat == 'y' or repeat == 'n':
            break
        else:
            print("Wrong data. Please enter 'y' or 'n'!")
    if repeat == 'y':
        continue
    else:
        print("Thank you! Good luck!")
        break
