def reverse_string(my_string):
    if len(my_string) == 0:
        return my_string
    return my_string[-1] + reverse_string(my_string[:-1])
print(reverse_string('name'))

