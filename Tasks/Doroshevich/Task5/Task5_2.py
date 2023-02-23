def reverse_string(list_of_strings):
    return [x[::-1] for x in list_of_strings]


while True:
    len_l = input("Enter the number of strings:\n")
    if len_l.isnumeric():
        l = [input(F"Enter string №{x+1}\n") for x in range(int(len_l))]
        break
    else:
        print("Wrong data. Please enter integer")

print(f"List of all reversed strings:\n{reverse_string(l)}")