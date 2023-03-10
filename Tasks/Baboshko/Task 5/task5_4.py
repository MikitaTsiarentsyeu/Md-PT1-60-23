def lower_upper(input_string):
    lower = 0
    upper = 0
    for i in range(len(input_string)):
        if input_string[i].islower():
            lower += 1
        elif input_string[i].isupper():
            upper += 1
    return lower, upper
print(lower_upper(input()))
