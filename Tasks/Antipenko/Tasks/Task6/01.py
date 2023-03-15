'''1. Write a recursive function to reverse a string.'''


def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string(string[1:]) + string[0]


example = 'comborambo'
print(reverse_string(example))
