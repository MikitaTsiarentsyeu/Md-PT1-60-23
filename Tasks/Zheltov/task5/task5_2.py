def reverse(my_list):
    new_string = ''
    for i in range(len(my_list)):
        new_string += my_list[-i-1]
    return new_string
print(reverse(['First', 'Second']))