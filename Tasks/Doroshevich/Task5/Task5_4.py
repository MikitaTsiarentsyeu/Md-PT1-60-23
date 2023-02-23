def low_up_case(string):
    lower = len([x for x in string if x.islower()])
    upper = len([x for x in string if x.isupper()])
    return lower, upper

s = input("Enter a string:\n")
print(f"count of lower case symbols is {low_up_case(s)[0]}\ncount of upper case symbols is {low_up_case(s)[1]}")