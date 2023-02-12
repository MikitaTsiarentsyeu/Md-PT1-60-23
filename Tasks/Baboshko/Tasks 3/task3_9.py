text_string = input('Пожалуйста, введите строку: \n')
new_string = ''
for i in range(len(text_string)-1, 0, -1):
    new_string = new_string + text_string[i]
new_string = new_string + text_string[0]
print(new_string)#swapcase быстрее, конечно)

#или так
x = -1
new_string_2 = ''
while x > -(len(text_string)+1):
    new_string_2 = new_string_2 + text_string[x]
    x -= 1
print(new_string, new_string_2, sep = '\n')