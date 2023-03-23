def g5_strings(list_of_strings):
    return [x for x in list_of_strings if len(x) > 5]


print("Enter the number of strings:")
while True:
    len_l = input()
    if len_l.isnumeric():
        l = [input(F"Enter string №{x+1}\n") for x in range(int(len_l))]
        break
    else:
        print("Wrong data. Please enter integer.")

print(
    f"list with all the strings that have a length greater than 5:\n{g5_strings(l)}")
